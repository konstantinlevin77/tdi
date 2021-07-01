import sys
from colorama import Fore
import importlib.util as iutil

# Import of List Entry
list_entry_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_spec)
list_entry_spec.loader.exec_module(ListEntryModule)

# Import of List Entry Dao
list_entry_dao_spec = iutil.spec_from_file_location("ListEntryDao","/home/konstantinlevin/Development/tdi/dataAccess/ListEntryDao.py")
ListEntryDaoModule = iutil.module_from_spec(list_entry_dao_spec)
list_entry_dao_spec.loader.exec_module(ListEntryDaoModule)

def load_list(list_entity):
    
    dao = ListEntryDaoModule.ListEntryDao("/home/konstantinlevin/Development/tdi/databases/tdi_database.db")

    entries = dao.getByListId(list_entity.id)

    entry_map = {str(i+1):entry for i,entry in enumerate(entries)}

    for num, entry in entry_map.items():
        print(num+"-",entry.entry_text+f"   [{'Done' if entry.done else 'Undone'}]")