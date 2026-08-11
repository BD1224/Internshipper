import database.database as db

def handle_clean(user_input):
    match user_input[1]:
        case "urls":
            db.clean_urls()
            print("\nURLs cleaned\n")
        case "words":
            db.clean_words()
            print("\nWords cleaned\n")
            
    return 0