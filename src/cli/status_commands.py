import database.database as db

def handle_status(user_input):
    match user_input[1]:
        case "on":
            db.status(True)
            print("\nStatus updates are on\n")
            return 3
        case "off":
            db.status(False)
            print("\nStatus updates are off\n")
            return 2
        case "set":
            if len(user_input) < 3:
                print("\nCommand failed\n")
                return 0
            time = user_input[2]
            
            output = db.set_time(time)
            if output==0:
                print("\nCommand failed\n")
            else:
                print(f"\nSet status update time to {time}\n")
                return 4
        case "show":
            status = db.get_status()
            time = db.get_time()
            print(f"\nStatus: {status}\nStatus update time: {time} (military time)\n")
            
    return 0