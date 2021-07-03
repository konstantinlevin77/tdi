import sys
from colorama import Fore
import importlib.util as iutil
import os

# Import of List Entry
list_entry_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_spec)
list_entry_spec.loader.exec_module(ListEntryModule)

# Import of List Entry Dao
list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)


def load_list(list_entity):

    os.system("clear")
    
    list_entry_dao = ListEntryDaoModule.ListEntryDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")

    entries = list_entry_dao.getByListId(list_entity.id)

    entry_map = {str(i+1):entry for i,entry in enumerate(entries)}

    print(Fore.LIGHTRED_EX+f"\n{list_entity.name}"+Fore.RESET)
    for num, entry in entry_map.items():
        print(Fore.MAGENTA + num+"-" + Fore.RESET,entry.entry_text+ Fore.CYAN + f"   [{'Done' if entry.done else 'Undone'}]" + Fore.RESET)
    
    print("\n\n"+Fore.LIGHTCYAN_EX+"You can use your list using commands below:")
    print(Fore.LIGHTYELLOW_EX+"done [ENTRY-ID] "+Fore.WHITE+" Marks as done the entry given")
    print(Fore.LIGHTYELLOW_EX+"undone [ENTRY-ID] "+Fore.WHITE+" Marks as undone the entry given")
    print(Fore.LIGHTYELLOW_EX+"add [ENTRY-TEXT] "+Fore.WHITE+" Adds entry to the current list")
    print(Fore.LIGHTYELLOW_EX+"remove [ENTRY-ID] "+Fore.WHITE+" Removes the entry given")
    print(Fore.LIGHTYELLOW_EX+"exit "+Fore.WHITE+" Exits the list.")

    return entry_map