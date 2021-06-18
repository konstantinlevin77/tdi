import sys
from colorama import Fore
import importlib.util as iutil

# Annoying import of TodoList class.
todolist_spec = iutil.spec_from_file_location("TodoList","/home/konstantinlevin/Development/tdi/entities/TodoList.py")
TodoListModule = iutil.module_from_spec(todolist_spec)
todolist_spec.loader.exec_module(TodoListModule)

# It's still annoying
list_dao_spec = iutil.spec_from_file_location("ListDao","/home/konstantinlevin/Development/tdi/dataAccess/ListDao.py")
ListDaoModule = iutil.module_from_spec(list_dao_spec)
list_dao_spec.loader.exec_module(ListDaoModule)



# First argument is the script itself for now so I'm adding 1 to find first argument, but it'll change.
TESTING_ARG = 1

# Second argument is 'create' itself so first create argument will be 
# sys.argv[0 + TESTING_ARG + COMMAND_ARG]
COMMAND_ARG = 1

def createList():
    
    print(Fore.GREEN + "Ahooy! It seems like you wanna create a new list, okay. First let's put a name to your list, you can change it later")
    print(Fore.RESET)

    dao = ListDaoModule.ListDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")
    
    name_determined = False
    list_name = ""
    while not name_determined:
        

        # In database first index (0) is id, second (1) is name.
        INDEX_OF_LIST_NAME = 1
        existingListNames = [entry[INDEX_OF_LIST_NAME] for entry in dao.getAll()]

        list_name = input(Fore.RED + "Your list's name:" + Fore.WHITE).strip()
        print(Fore.RESET)
        
        if list_name == "":
            print(Fore.YELLOW + "Sorry, but your list's name can't be blank.")

        elif list_name in existingListNames:
            print(Fore.YELLOW + "Sorry, but there is a list with this name, list's name must be unique.")

        else:
            print(Fore.CYAN + "What a good choice: '{}' ".format(list_name))
            print(Fore.RESET)
            name_determined = True


    print(Fore.RESET+"\n")
    print(Fore.GREEN + "Alright, if you want to make your list more secure you might create a password for it, but please make sure that you don't forget it, if you forget you won't be able to get your list again. However if you don't want to create a password, just hit enter.")
    password = input(Fore.RED + "Your list's passowrd:" + Fore.WHITE).strip()

    dao.add(TodoListModule.TodoList(list_name,password))
    print(Fore.GREEN + "Fascinating! Your new list '{}' is ready, you can start to work with it by typing\n".format(list_name))
    print(Fore.RESET)
    print(Fore.MAGENTA + "\ttdi open list \"{}\"".format(list_name))
    print(Fore.RESET)



create_arguments = {
    "list":createList
}


def create():

    if len(sys.argv) == 0 + TESTING_ARG + COMMAND_ARG:
        print(Fore.LIGHTYELLOW_EX + "You did not specified what you wanted to create, did you mean\n")
        print(Fore.RESET + Fore.LIGHTGREEN_EX + "\tcreate list")
        print(Fore.RESET)
    
    else:
        current_create_argument = sys.argv[0 + TESTING_ARG + COMMAND_ARG]
        current_create_command = create_arguments.get(current_create_argument)

        if current_create_command is None:
            print(Fore.YELLOW + "Sorry, but for now you can't create a new '{}'\n".format(current_create_argument))
            print(Fore.RESET + Fore.CYAN + "But you can still create a new {}".format(str(*list(create_arguments.keys()))))
            print(Fore.RESET)
        else:
            current_create_command()

        
