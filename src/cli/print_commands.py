import database.database as db

def handle_print(user_input):
    match user_input[1]:
        case "prev":
            db.print_prev()
        case "words":
            db.print_words()
        case "gwords":
            db.print_global_words()
        case "ngwords":
            db.print_non_global_words()
        case "urls":
            db.print_data()
            
    return 0