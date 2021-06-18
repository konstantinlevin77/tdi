import importlib.util as iutil

list_entry_module_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_module_spec)
list_entry_module_spec.loader.exec_module(ListEntryModule)

class ListEntryDao():
    
    def __init__(self,db_path):
        self.db_path = db_path
