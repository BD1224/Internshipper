import shlex  # used to handle inputs with quotes
from .handler import handle_input
from prompt_toolkit import prompt

def display(status_on_flag, lock):
    print(
        "************************************************\n"
        "Welcome to internshipper! Type help for commands\n"
        "************************************************\n"
    )

    while True:
        try:  # shlex may throw an error if there is an unclosed quote
            user_input = shlex.split(prompt(">> ").lower())  # user_input is a list of inputs
            with lock: # needed so print statements dont collide with other thread
                output = handle_input(user_input)
                if output == 1:  # user typed close
                    return 0
                if output == 2:  # user typed status off
                    status_on_flag.clear()
                if output == 3:  # user typed status on
                    status_on_flag.set()
        except (EOFError, KeyboardInterrupt):
            print()  # EOF doesnt go to a new line when continuing, neither does ^C
            continue
        except:
            continue