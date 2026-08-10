import database.database as db

def handle_url(user_input):
    match user_input[1]:
        case "add":
            output = db.add_url(user_input[2])
            if output==0:
                print("\n\ndid not add\n\n")
            else:
                print("\n\nadded\n\n")
        case "rid":
            output = db.remove_url(user_input[2])
            if output==0:
                print("\n\ndid not remove\n\n")
            else:
                print("\n\nremoved\n\n")
        case "gid":
            if len(user_input) < 4:
                print("\n\ncommand failed\n\n")
                return 0
            output = db.include_global_words(user_input[2], user_input[3])
            if output==0:
                print("\n\ndid not remove\n\n")
            else:
                print("\n\nremoved\n\n")
        case "print":
            db.print_url_id(user_input[2])
            
    return 0