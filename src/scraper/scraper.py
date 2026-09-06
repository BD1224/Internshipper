import requests  # to download pages html
from playwright.sync_api import sync_playwright  # fallback if requests doesnt work
from bs4 import BeautifulSoup  # to parse that html
from database.database import increment_consecutive_fails, get_consecutive_fails

def scrape(URL, words):  # returns tuple, for easier parsing of result
    if get_consecutive_fails(URL) < 3:
        result = request_scrape(URL, words)
        if result[0] == 0:
            print("REQUESTS FAILED\n")
            increment_consecutive_fails(URL)
        if result[0] == 2:
            return result
    print("USED PLAYWRITE\n")
    return playwright_scrape(URL, words)

def request_scrape(URL, words):
    try:
        html = requests.get(URL, timeout=10)  # fetches web page
        status = html.raise_for_status()  # checks for failure, throws error if failed
        return check_text(html.text, words)
    except:
        return (0,)  # error

def playwright_scrape(URL, words):
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(URL, wait_until="networkidle", timeout=10000)
            html = page.content()  # rendered html, after js has run
            return check_text(html, words)
        except:
            return (0,)  # error
        finally:
            browser.close()  # browser always closes

def check_text(html, words):
    soup = BeautifulSoup(html, "html.parser")  # creates soup object used to parse
    text = soup.get_text(" ", strip=True).lower()  # creates string w/o html syntax

    blocked = any(invalid in text for invalid in ["captcha", "access denied", "verify you are human"])
    if blocked or len(text) < 500:
        raise Exception

    for word in words:
        if word in text:
            return (2, word)  # a word found!

    return (1,)  # no error no word found