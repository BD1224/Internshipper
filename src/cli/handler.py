import src.cli.url_commands as uc
import src.cli.word_commands as wc
import src.cli.print_commands as pc
import src.cli.misc_commands as mc


def handle_input(user_input):

    match user_input[0]:  # automatically breaks unlike C/Java
        case "close":
            mc.print_close()
        case "help":
            mc.print_help()
        case "inst":
            mc.print_inst()
        case "clear":
            mc.clear()
        case "deleteall":
            mc.delete()
        case "url":
            if len(user_input) < 3:
                print("\n\ncommand failed\n\n")
                return 0
            uc.handle_url(user_input)
        case "word":
            if len(user_input) < 3:
                print("\n\ncommand failed\n\n")
                return 0
            wc.handle_word(user_input)
        case "print":
            if len(user_input) < 2:
                print("\n\ncommand failed\n\n")
                return 0
            pc.handle_print(user_input)

    return 0





