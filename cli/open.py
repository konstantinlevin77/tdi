import sys
from colorama import Fore
import importlib.util as iutil
import os

from load_list import load_list
from run_open_interpreter import run_open_interpreter

from is_test import is_test

# Import of List Entry
list_entry_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_spec)
list_entry_spec.loader.exec_module(ListEntryModule)

# Import of List Dao
list_dao_spec = iutil.spec_from_file_location("ListDao","/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)

# I run mainHandler.py script as python mainHandler.py, so the first system argument
# is script itself.# Import of List Entry Dao
list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)
TESTING_ARG = is_test()

# Second argument is "open" command itself so in order to get the first open argument we 
# should sys.argv[0 + TESTING_ARG + OPEN_ARG]
OPEN_ARG = 1


def open_list():

    list_dao = ListDaoModule.ListDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")

    # Third argument is "list" itself so in order to get which list
    # user wants to open we should start from index [0 + TESTING_ARG + OPEN_ARG + LIST_ARG]
    LIST_ARG = 1

    if len(sys.argv) == 0 + TESTING_ARG + OPEN_ARG + LIST_ARG:
        print(Fore.GREEN + "Sorry, you did not give the name of the list you want to open.")
        print(Fore.RESET)
        return

    name_of_list_to_open = " ".join(sys.argv[0 + TESTING_ARG + OPEN_ARG + LIST_ARG:len(sys.argv)])
    
    entity_of_list_to_open = list_dao.getByName(name_of_list_to_open)

    if entity_of_list_to_open.id is None:
        print(Fore.CYAN + f"You did not create the list '{name_of_list_to_open}' yet, but you can create it by typing")
        print(Fore.LIGHTRED_EX + f"\ttdi create list '{name_of_list_to_open}'")
        print(Fore.RESET)

    else:
        entity_map = load_list(entity_of_list_to_open)
        run_open_interpreter(entity_of_list_to_open,entity_map)


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
            current_open_command()




