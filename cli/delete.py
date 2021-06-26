import sys
from colorama import Fore
import importlib.util as iutil

"""Import of TodoList entity."""
todolist_spec = iutil.spec_from_file_location("TodoList","/home/konstantinlevin/Development/tdi/entities/TodoList.py")
TodoListModule = iutil.module_from_spec(todolist_spec)
todolist_spec.loader.exec_module(TodoListModule)

"""Import of TodoListDao data access object"""
list_dao_spec = iutil.spec_from_file_location("ListDao","/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)

"""Import of ListEntry data access object"""
list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)

# For now I'm running script as python3 mainHandler.py so the first argument is script itself.
TESTING_ARG = 1

# Second argument is python3 mainHandler.py "create" so the second argument is command itself.
COMMAND_ARG = 1


def delete_list():
    pass

delete_arguments = {
    "list": delete_list
}

def delete():
    if len(sys.argv) == 0 + TESTING_ARG + COMMAND_ARG:
        print(Fore.LIGHTYELLOW_EX + "You did not specified what you wanted to delete, did you mean")
        print(Fore.RESET)
        print(Fore.CYAN + "\tdelete list")
        print(Fore.RESET)
    
    else:
        current_delete_argument = sys.argv[0 + TESTING_ARG + COMMAND_ARG]
        current_delete_command = delete_arguments.get(current_delete_argument)

        if current_delete_command is None:
            print(Fore.YELLOW + f"Sorry but for now you can't delete a {current_delete_argument}, but you can still delete a list.")
            print(Fore.RESET)

        else:
            current_delete_command()
