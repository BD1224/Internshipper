import shlex  # used to handle inputs with quotes
from .handler import handle_input

def display(recent_print_flag, lock):

    print(
        "************************************************\n"
        "Welcome to internshipper! Type help for commands\n"
        "************************************************\n"
    )

    while True:
        try:  # shlex may throw an error if there is an unclosed quote
            user_input = shlex.split(input(">> ").lower())  # user_input is a list of inputs
            if recent_print_flag.is_set():
                user_input = ""  # not necessary but just in case
                print()
                recent_print_flag.clear()  # resets flag
            else:
                with lock: # needed so it doesnt collide with other thread
                    output = handle_input(user_input)
                    if output == 1:  # user typed close
                        return 0
        except (EOFError, KeyboardInterrupt):
            print()  # EOF doesnt go to a new line when continuing, neither does ^C
            continue
        except:
            continue