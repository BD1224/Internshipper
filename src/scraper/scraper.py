import requests  # to download pages html
from bs4 import BeautifulSoup  # to parse that html

def scrape(URL, words):
    try:
        html = requests.get(URL, timeout=10)  # fetches web page
        status = html.raise_for_status()  # checks for failure
    except:
        return 0  # error

    soup = BeautifulSoup(html.text, "html.parser")  # parses into words
    text = soup.get_text(" ", strip=True).lower()  # creates list of words, in lowercase

    for word in words:
        if word in text:
            return 2  # a word found!
     
    return 1  # no error no word found