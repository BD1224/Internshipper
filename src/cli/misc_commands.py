def print_help():
    print("""
        \nCommands:\n\n
        url add <url>: adds <url> to list of tracked urls\n
        url rid <id>: removes url listed as <id>\n
        url gid <id> <t or f>: sets whether url listed as <id> uses(t) or ignores(f) global words\n
        url print <id>: prints the url with corresponding <id>\n\n
        word add <id> <word>: adds <word> to be tracked by url listed as <id>\n
        word rid <id>: removes word listed as <id> (different from url id)\n
        word r <word>: removes <word>, this will remove all occurences of <word>\n
        word gadd <word>: adds <word> to be tracked globally\n\n
        print prev: prints previous result\n
        print words: prints all words tracked\n
        print gwords: prints all global words\n
        print ngwords: prints all non-global words\n
        print urls: prints urls and their data\n\n
        close: stops application from running\n
        help: gets you here\n
        inst: displays instructions\n\n
    """)

def print_inst():
    print("""AI will write this later""")


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
