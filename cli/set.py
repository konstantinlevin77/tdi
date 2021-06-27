import sys
from colorama import Fore
import importlib.util as iutil

"""Import of TodoList entity."""
todo_list_spec = iutil.spec_from_file_location(
    "TodoList", "/home/konstantinlevin/Development/tdi/entities/TodoList.py")
TodoListModule = iutil.module_from_spec(todo_list_spec)
todo_list_spec.loader.exec_module(TodoListModule)

"""Import of TodoList Data Access Object"""
todo_list_dao_spec = iutil.spec_from_file_location(
    "ListDao", "/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
TodoListDaoModule = iutil.module_from_spec(todo_list_dao_spec)
todo_list_dao_spec.loader.exec_module(TodoListDaoModule)

# I run this script "python3 mainHandler.py" so for test time first argument is script itself.
TESTING_ARG = 1

# Second argument is python3 mainHandler.py "set"
# so if we want to get the first set argument we should sys.argv[0 + TESTING_ARG + SET_ARG]
SET_ARG = 1

dao = TodoListDaoModule.ListDao(
    "/home/konstantinlevin/Development/tdi/databases/tdi_database.db")


def set_list_name():
    print(Fore.LIGHTMAGENTA_EX + "Okayy, let's set some name stuff, first of all can you give me the name of the list you want to set the password")
    list_name = input(Fore.RED + "List's Name:" + Fore.WHITE).strip()

    all_lists_names = [s.name for s in dao.getAll()]

    if list_name in all_lists_names:
        lists_password = dao.getByName(list_name).password

        if lists_password != "":
            print(Fore.CYAN + "This list has a password, so you should type the old password before setting a new one")
            while True:
                lists_password_given_by_user = input(
                    Fore.LIGHTRED_EX + "List's Password:"+Fore.RESET).strip()
                if lists_password_given_by_user == lists_password:
                    break

        print(Fore.CYAN + "Now please give the new name of this list.")
        new_name = input(Fore.LIGHTRED_EX + "New Name:" + Fore.RESET)

        entity_version_of_set_list = dao.getByName(list_name)
        entity_version_of_set_list.name = new_name
        dao.update(entity_version_of_set_list)

        print(Fore.LIGHTGREEN_EX + "Your list's name has been setted :)")
        print(Fore.RESET)

    else:
        print(
            Fore.CYAN + f"You don't have a list called '{list_name}', however you can create it by typing")
        print(Fore.LIGHTGREEN_EX + "\ttdi create list")


def set_list_password():
    print(Fore.LIGHTMAGENTA_EX + "Okayy, let's set some password stuff, first of all can you give me the name of the list you want to set the password")
    list_name = input(Fore.RED + "List's Name:" + Fore.WHITE).strip()

    all_lists_names = [s.name for s in dao.getAll()]

    if list_name in all_lists_names:
        lists_password = dao.getByName(list_name).password

        if lists_password != "":
            print(Fore.CYAN + "This list has a password, so you should type the old password before setting a new one")
            while True:
                lists_password_given_by_user = input(
                    Fore.LIGHTRED_EX + "List's Password:"+Fore.RESET).strip()
                if lists_password_given_by_user == lists_password:
                    break

        print(Fore.CYAN + "Now please give the new password")
        new_password = input(Fore.LIGHTRED_EX + "New Password:" + Fore.RESET)

        entity_version_of_set_list = dao.getByName(list_name)
        entity_version_of_set_list.password = new_password
        dao.update(entity_version_of_set_list)

        print(Fore.LIGHTGREEN_EX + "Your list's password has been setted :)")
        print(Fore.RESET)

    else:
        print(
            Fore.CYAN + f"You don't have a list called '{list_name}', however you can create it by typing")
        print(Fore.LIGHTGREEN_EX + "\ttdi create list")


set_list_arguments = {
    "name": set_list_name,
    "password": set_list_password
}


def set_list():
    # So the fourth argument will be what user want to set
    INDEX_OF_ARGUMENT_TO_SET = 1

    current_argument_to_set = sys.argv[0 +
                                       TESTING_ARG + SET_ARG + INDEX_OF_ARGUMENT_TO_SET]
    current_argument_command = set_list_arguments.get(current_argument_to_set)

    if current_argument_command is None:
        print(
            Fore.CYAN + f"Sorry but for now you can set the '{current_argument_to_set}' property of a list, but you can still set name or password.")
        print(Fore.RESET)

    else:
        current_argument_command()


set_arguments = {
    "list": set_list
}


def set_():

    if len(sys.argv) == 0 + TESTING_ARG + SET_ARG:

        print(Fore.CYAN + "Sorry but you did not specified what you wanted to set, did you mean")
        print(Fore.RESET)
        print(Fore.LIGHTRED_EX + "\ttdli set list" + Fore.RESET)
        return

    current_argument = sys.argv[0 + TESTING_ARG + SET_ARG]
    current_set_command = set_arguments.get(current_argument)

    if current_set_command is None:
        print(
            Fore.CYAN + f"Sorry but for now you can't set properties of a {current_argument}, but you can still set the properties of a list.")
        print(Fore.RESET)

    else:
        current_set_command()
