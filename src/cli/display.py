from .handler import handle_input

def display():
    # Note: this uses implicit string conc
    print(
        "************************************************\n"
        "Welcome to internshipper! Type help for commands\n"
        "************************************************\n"
    )

    while True:
        user_input = input(">> ").lower().split() # user_input is list of inputs
        output = handle_input(user_input)