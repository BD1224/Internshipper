from config import RED, GREEN, RESET
from .scraper import scrape
from database.database import get_urls, get_words, get_global_words, update_prev_print, found_application

from prompt_toolkit import print_formatted_text  # used to bypass the patch_stdout control of the ANSI codes
from prompt_toolkit.formatted_text import ANSI

def provide_status():
    print_out = ""
    for row in get_urls():
        site_id = row[0]  # id
        URL = row[1]
        words = get_global_words() + get_words(site_id)  # did it this way to separate db from logic
        words = [word[2] for word in words]  # separates out just the word text
        result = scrape(URL, words)
        output = result[0]
        print_out += f"\n{URL}\n"
        if output == 0:  # exited with error
            print_out += f"\t{RED}Error: unable to fetch{RESET}"
        elif output == 1:  # no words found
            print_out += f"\tNo application found"
        elif output == 2:  # word found
            print_out += f"\t{GREEN}\"{result[1]}\" found!{RESET}"
            found_application(URL)
    print_out += "\n"
    print_formatted_text(ANSI(print_out))
    update_prev_print(print_out)  # updates variable to be used in cli