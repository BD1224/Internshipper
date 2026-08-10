import database.database as db

def handle_word(user_input):
    match user_input[1]:
        case "add":
            if len(user_input) < 4:
                print("\nCommand failed\n")
                return 0
            output = db.add_word(user_input[2], user_input[3])
            if output==0:
                print("\nDid not add\n")
            else:
                print("\nAdded\n")
        case "rid":
            output = db.remove_word_id(user_input[2])
            if output==0:
                print("\nDid not remove\n")
            else:
                print("\nRemoved\n")
        case "r":
            output = db.remove_word(user_input[2])
            if output==0:
                print("\nDid not remove\n")
            else:
                print("\nRemoved\n")
        case "gadd":
            output = db.add_global_word(user_input[2])
            if output==0:
                print("\nDid not add\n")
            else:
                print("\nAdded\n")

    return 0