import sys
from colorama import Fore
import importlib.util as iutil
import os

list_entry_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_spec)
list_entry_spec.loader.exec_module(ListEntryModule)

# I run mainHandler.py script as python mainHandler.py, so the first system argument
# is script itself.
TESTING_ARG = 1

# Second argument is "open" command itself so in order to get the first open argument we 
# should sys.argv[0 + TESTING_ARG + OPEN_ARG]
OPEN_ARG = 1


def open_list():
    pass


open_arguments = {
    "list":open_list
}

def open():
    if len(sys.argv) == 0 + TESTING_ARG + OPEN_ARG:
        print(Fore.CYAN + "You did not specified what you wanted to open, did you mean")
        print(Fore.YELLOW + "\ttdi open list")

    else:
        current_open_argument = sys.argv[0 + TESTING_ARG + OPEN_ARG]
        current_open_command = open_arguments.get(current_open_argument)
        if current_open_command is None:
            print(Fore.CYAN + f"Sorry :(, You can't open a '{current_open_argument}' right now, but you can still open a list.")
            print(Fore.RESET)
        else:
            current_open_command




