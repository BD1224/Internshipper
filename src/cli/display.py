import shlex  # used to handle inputs with quotes
from .handler import handle_input

def display():
    # Note: this uses implicit string conc
    print(
        "************************************************\n"
        "Welcome to internshipper! Type help for commands\n"
        "************************************************\n"
    )

    while True:
        try:  # shlex may throw an error if there is an unclosed quote
            user_input = shlex.split(input(">> ").lower())  # user_input is a list of inputs
            output = handle_input(user_input)
        except ValueError:  # used ValueError to avoid ^C bug, where it doesnt exit
            continue