import database.database as db

def handle_word(user_input):
    match user_input[1]:
        case "add":
            if len(user_input) < 4:
                print("\n\ncommand failed\n\n")
                return 0
            output = db.add_word(user_input[2], user_input[3])
            if output==0:
                print("\n\ndid not add\n\n")
            else:
                print("\n\nadded\n\n")
        case "rid":
            output = db.remove_word_id(user_input[2])
            if output==0:
                print("\n\ndid not remove\n\n")
            else:
                print("\n\nremoved\n\n")
        case "r":
            output = db.remove_word(user_input[2])
            if output==0:
                print("\n\ndid not remove\n\n")
            else:
                print("\n\nremoved\n\n")
        case "gadd":
            output = db.add_global_word(user_input[2])
            if output==0:
                print("\n\ndid not add\n\n")
            else:
                print("\n\nadded\n\n")

    return 0