import sys
from colorama import Fore
import importlib.util as iutil

list_dao_spec = iutil.spec_from_file_location("ListDao","/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)

list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)

# For now I'm running mainHandler.py script as $python3 ./mainHandler.py so first argument is 
# script itself but I'll remove it deployment time.
TESTING_ARG = 1

# Second argument is "clean" command itself so first clean argument will be args[0 + TESTING_ARG + CLEAN_ARG]
CLEAN_ARG = 1

list_dao = ListDaoModule.ListDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")
list_entry_dao = ListEntryDaoModule.ListEntryDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")


def clean_list():
    # Third argument will be the thing to clear. Such as for now it's a list, so to get the name of
    # the thing we clear we need to get 0 + TESTING_ARG + CLEAN_ARG + ARGUMENT_TO_CLEAR : -1
    ARGUMENT_TO_CLEAR = 1
    name_of_to_clear = " ".join(sys.argv[0 + TESTING_ARG + CLEAN_ARG + ARGUMENT_TO_CLEAR:len(sys.argv)])

    # entry[0] is id.
    all_list_names = [entry.name for entry in list_dao.getAll()]
    if name_of_to_clear in all_list_names:
        
        id_of_to_clear = list_dao.getByName(name_of_to_clear).id
        list_entry_dao.deleteByListId(id_of_to_clear)
        print(Fore.LIGHTGREEN_EX + "Alright, all entries of your list have been cleaned!")


    else:
        print(Fore.LIGHTMAGENTA_EX + "There is no list with this name, would you like to create it by typing")
        print(Fore.LIGHTBLUE_EX + "\ttdi create list {}".format(name_of_to_clear))




clean_arguments = {"list":clean_list}

def clean():
    current_argument = sys.argv[0 + TESTING_ARG + CLEAN_ARG]
    current_command = clean_arguments.get(current_argument)

    if current_command is None:
        print(Fore.CYAN + f"Sorry, but you can't clean a \"{current_argument}\" for now, but you can still clean a list. ")
        print(Fore.RESET)

    else:
        current_command()


