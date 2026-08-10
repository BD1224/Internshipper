from config import RED, GREEN, RESET, SCRAPING_FREQUENCY
from .scraper import scrape
from database.database import get_urls, get_words, get_global_words, update_prev_print, found_application
import time

def provide_status():
    while True:
        print_out = ""
        for row in get_urls():
            site_id = row[0]  # id
            URL = row[1]
            words = get_global_words() + get_words(site_id)  # did it this way to separate db from logic
            words = [word[2] for word in words]  # separates out just the word text
            output = scrape(URL, words)
            print_out += f"\n{URL}\n"
            if output == 0:  # exited with error
                print_out += f"\t{RED}Error: unable to fetch{RESET}"
            elif output == 1:  # no words found
                print_out += f"\tNo application found"
            elif output == 2:  # word found
                print_out += f"\t{GREEN}Application found!{RESET}"
                found_application(URL)
        print_out += "\n"
        print(f"{print_out}")
        update_prev_print(print_out)  # updates variable to be used in cli
        time.sleep(5)  # SCRAPING_FREQUENCY*60*60