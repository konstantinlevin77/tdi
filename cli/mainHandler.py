from colorama import Fore
import sys
import os


from clean import clean
from create import create
from delete import delete
from open import open
from set import set_
from getall import getall

from is_test import is_test

commands = {
    "clean":clean,
    "create":create,
    "delete":delete,
    "open":open,
    "set":set_,
    "getall":getall
    }

# First argument is the script itself for now so I'm adding 1 to find first argument, but it'll change.
TESTING_ARG = is_test()


def main():
    if len(sys.argv) == 0 + TESTING_ARG:
        print(Fore.YELLOW+ "Hey, it seems like you did pass no commands, you can get help by typing\n" + Fore.RESET + Fore.LIGHTYELLOW_EX + "\ttdi --help")
        print(Fore.RESET)

    else:
        current_command_arg = sys.argv[0 + TESTING_ARG]
        command = commands.get(current_command_arg)
        if command is None:

            print(Fore.CYAN +"Sorry but for now there is no command called '{}'".format(current_command_arg))
            print(Fore.RESET)

        else:
            command()

        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.CYAN + "Program terminated." + Fore.RESET)