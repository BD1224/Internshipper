import requests  # to download pages html
from bs4 import BeautifulSoup  # to parse that html

def scrape(URL, words):  # returns tuple, for easier parsing of result
    try:
        html = requests.get(URL, timeout=10)  # fetches web page
        status = html.raise_for_status()  # checks for failure
    except:
        return (0,)  # error

    soup = BeautifulSoup(html.text, "html.parser")  # creates soup object used to parse
    text = soup.get_text(" ", strip=True).lower()  # creates string w/o html syntax

    for word in words:
        if word in text:
            return (2, word)  # a word found!
     
    return (1,)  # no error no word found