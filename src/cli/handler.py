import src.cli.url_commands as uc
import src.cli.word_commands as wc
import src.cli.print_commands as pc
import src.cli.misc_commands as mc
import src.cli.clean_commands as cc
import src.scraper.provide_status as sc


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
        case "run":
            sc.run()
        case "url":
            if len(user_input) < 3:
                print("\nCommand failed\n")
                return 0
            uc.handle_url(user_input)
        case "word":
            if len(user_input) < 3:
                print("\nCommand failed\n")
                return 0
            wc.handle_word(user_input)
        case "print":
            if len(user_input) < 2:
                print("\nCommand failed\n")
                return 0
            pc.handle_print(user_input)
        case "clean":
            if len(user_input) < 2:
                print("\nCommand failed\n")
                return 0
            cc.handle_clean(user_input)

    return 0





