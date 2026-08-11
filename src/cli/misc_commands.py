def print_help():
    print("""
Commands:\n
url add <url>: adds <url> to list of tracked urls
url remove <id>: removes url with <id>
url global <id> <t or f>: enables(t) or disables(f) global words for the url with <id>
url print <id>: prints the url with <id>\n
word add <id> <word>: adds <word> to the url with <id>
word remove <id>: removes words with <id> 
word removeall <word>: removes all occurences of <word>
word gadd <word>: adds <word> as a global word\n
print prev: prints previous result
print words: prints all tracked words
print gwords: prints all global words
print ngwords: prints all non-global words
print urls: prints urls and their data\n
clean urls: permanently removes urls which have found a word
clean words: removes non-global words whose urls are non-existent or found a word\n
close: stops application from running
help: gets you here
inst: displays instructions
clear: clears screen
run: immediately checks all tracked URLs for any tracked words or phrases.
    """)

def print_inst():
    from config import SCRAPING_FREQUENCY
    print(f"""
To use The Internshipper, first go to a company's career page and search for
"intern" and, if you want, a specific location. Copy the URL of the resulting
search page and add it to the program. Then add words such as "software",
"finance", or "analyst" so the program knows what to look for on that page.
A global word is a word that every global URL searches for. A non-global word
is assigned to only one specific URL, meaning only that URL searches for it.
A non-global URL does not search for any global words and will only search for
the words specifically assigned to that URL.
The program checks each URL every {SCRAPING_FREQUENCY} hours and displays the status
or outcome of each search. Once a URL finds one of its search words, it will
no longer appear in the normal status display. You can still view URLs that
have already found a match by using the appropriate display commands.
""")


def print_close():
    print("\nClosing Internshipper . . .\n")
    # FIGURE OUT HOW TO END ALL PROCESSES

def delete():
    import database.database as db
    print("\nAre you sure? (Type 'y' to confirm and any other key to exit):")
    answer = input().lower()
    if answer == 'y':
        db.delete_all()
        print("Everything deleted\n")
    else:
        print("Did not delete\n")

def clear():
    import sys
    sys.stdout.write("\033[2J\033[H\033[3J")  # clears screen, sets cursor to top left and removes scrollback
    sys.stdout.flush()  # handles anything in buffer
