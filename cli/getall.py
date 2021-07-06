import sys
from colorama import Fore
import importlib.util as iutil

list_dao_spec = iutil.spec_from_file_location(
    "ListDao", "/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)

# I run this script "python mainHandler.py x x" so the first argument is script itself.
TESTING_ARG = 1

# The second argument is "getall" command itself, so in order to get first argument
# sys.argv[0 + TESTING_ARG + GETALL_ARG]
GETALL_ARG = 1


def lists_command():
    pass


getall_arguments = {"lists": lists_command}


def getall():

    arg_to_get_all = sys.argv[0 + TESTING_ARG + GETALL_ARG]

    current_command = getall_arguments.get(arg_to_get_all)

    if current_command is None:
        print(Fore.LIGHTRED_EX +
              f"Sorry, but for now you can't get all {arg_to_get_all}, but you can still get all lists.")
        print(Fore.RESET)

    else:
        pass
