import importlib.util as iutil

from executeQuery import executeQuery

list_entry_module_spec = iutil.spec_from_file_location("ListEntry","/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_module_spec)
list_entry_module_spec.loader.exec_module(ListEntryModule)

class ListEntryDao():
    
    def __init__(self,db_path):
        self.db_path = db_path
    

    def add(self,list_entry:ListEntryModule.ListEntry):
        QUERY = "INSERT INTO list_entries(list_id,entry_text,done) VALUES(?,?,?)"
        params = (list_entry.list_id,list_entry.entry_text,list_entry.done)
        executeQuery(self.db_path,QUERY,params=params)

    
    def addAll(self,list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.add(list_entry)
    
