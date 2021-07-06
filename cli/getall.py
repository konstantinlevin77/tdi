import sys
from colorama import Fore
import importlib.util as iutil

list_dao_spec = iutil.spec_from_file_location(
    "ListDao", "/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)

list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)

# I run this script "python mainHandler.py x x" so the first argument is script itself.
TESTING_ARG = 1

# The second argument is "getall" command itself, so in order to get first argument
# sys.argv[0 + TESTING_ARG + GETALL_ARG]
GETALL_ARG = 1

dao = ListDaoModule.ListDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")
list_entry_dao = ListEntryDaoModule.ListEntryDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")

def lists_command():
    all_lists = dao.getAll()
    num_of_entries = [len(list_entry_dao.getByListId(a.id)) for a in all_lists]
    max_name_length = max([len(s.name) for s in dao.getAll()])
    max_password_length = max([0 if s.password == None  else len(s.password) for s in dao.getAll()])

    print(Fore.CYAN + "\tAll Lists!" + Fore.RESET)
    print(Fore.YELLOW+"NAME | PASSWORD | NUMBER OF ENTRIES")
    print(Fore.RESET)
    for i,list_sample in enumerate(all_lists):
        
        if list_sample.id == None:
            return
        
        if list_sample.password == None:
            list_sample.password = ""

        print(Fore.MAGENTA + list_sample.name+Fore.RESET+" "*(max_name_length-len(list_sample.name))+"*"*len(list_sample.password)+" "*(max_password_length-len(list_sample.password))+" "+str(num_of_entries[i]))


getall_arguments = {"lists": lists_command}


def getall():

    arg_to_get_all = sys.argv[0 + TESTING_ARG + GETALL_ARG]

    current_command = getall_arguments.get(arg_to_get_all)

    if current_command is None:
        print(Fore.LIGHTRED_EX +
              f"Sorry, but for now you can't get all {arg_to_get_all}, but you can still get all lists.")
        print(Fore.RESET)

    else:
        current_command()
