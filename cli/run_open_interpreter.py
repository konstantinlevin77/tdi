from colorama import Fore
import importlib.util as iutil
from load_list import load_list

# Import of List Entry
list_entry_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_spec)
list_entry_spec.loader.exec_module(ListEntryModule)

# Import of List Entry Dao
list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)

dao = ListEntryDaoModule.ListEntryDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")

def done_command(args,entry_map,list_entity):
    arg_to_get_done = args[0]

    if arg_to_get_done in entry_map.keys():

        entry_to_done = entry_map[arg_to_get_done]
        entry_to_done.done = 1
        dao.update(entry_to_done)
        entry_map = load_list(list_entity)
        print(Fore.CYAN + "Entry marked as done!" + Fore.RESET)

    else:
        print(Fore.RED+"There is no entry with id {}".format(arg_to_get_done))


    return entry_map

def undone_command(args,entry_map,list_entity):
    pass

def add_command(args,entry_map,list_entity):
    pass

def remove_command(args,entry_map,list_entity):
    pass

def exit_command(args):
    pass

interpreter_commands = {
    "done":done_command,
    "undone":undone_command,
    "add":add_command,
    "remove":remove_command,
    "exit":exit_command
}

def run_open_interpreter(list_entity,entry_map):
    while True:

        raw_command = input(Fore.YELLOW+"Type your command: "+Fore.RESET)
        command,args = raw_command.split()[0],raw_command.split()[1:len(raw_command.split())]

        command_as_function = interpreter_commands.get(command)

        if command_as_function is None:
            print(Fore.RESET)
            print(Fore.RED+f"There is no command called {command}")

        else:
            entry_map = command_as_function(args,entry_map,list_entity)
        
        