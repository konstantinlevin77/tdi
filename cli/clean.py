import sys
from colorama import Fore

# For now I'm running mainHandler.py script as $python3 ./mainHandler.py so first argument is 
# script itself but I'll remove it deployment time.
TESTING_ARG = 1

# Second argument is "clean" command itself so first clean argument will be args[0 + TESTING_ARG + CLEAN_ARG]
CLEAN_ARG = 1

def clean_list():
    pass


clean_arguments = {"list":clean_list}

def clean():
    current_argument = sys.argv[0 + TESTING_ARG + CLEAN_ARG]
    current_command = clean_arguments.get(current_argument)

    if current_command is None:
        print(Fore.CYAN + f"Sorry, but you can't clean a \"{current_argument}\" for now, but you can still clean a list. ")
        print(Fore.RESET)

    else:
        current_command()


