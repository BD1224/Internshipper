import database.database as db

def handle_url(user_input):
    match user_input[1]:
        case "add":
            output = db.add_url(user_input[2])
            if output==0:
                print("\nDid not add\n")
            else:
                print("\nAdded\n")
        case "remove":
            output = db.remove_url(user_input[2])
            if output==0:
                print("\nDid not remove\n")
            else:
                print("\nRemoved\n")
        case "global":
            if len(user_input) < 4:
                print("\nCommand failed\n")
                return 0
            output = db.include_global_words(user_input[2], user_input[3])
            if output==0:
                print("\nDid not update\n")
            else:
                print("\nUpdated\n")
        case "print":
            db.print_url_from_id(user_input[2])
            
    return 0