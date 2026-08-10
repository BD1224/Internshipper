def print_help():
    print("""
Commands:\n
url add <url>: adds <url> to list of tracked urls
url rid <id>: removes url listed as <id>
url gid <id> <t or f>: sets whether url listed as <id> uses(t) or ignores(f) global words
url print <id>: prints the url with corresponding <id>\n
word add <id> <word>: adds <word> to be tracked by url listed as <id>
word rid <id>: removes word listed as <id> (different from url id)
word r <word>: removes <word>, this will remove all occurences of <word>
word gadd <word>: adds <word> to be tracked globally\n
print prev: prints previous result
print words: prints all words tracked
print gwords: prints all global words
print ngwords: prints all non-global words
print urls: prints urls and their data\n
close: stops application from running
help: gets you here
inst: displays instructions
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
