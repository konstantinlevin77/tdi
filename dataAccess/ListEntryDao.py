import importlib.util as iutil

import sqlite3

def executeQuery(db_path,query,params=None,select=False):

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute(query,params)
        if select:
            res = cursor.fetchall()
            connection.close()
            return res

        else:
            connection.commit()
            connection.close()
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

    
    def update(self,list_entry:ListEntryModule.ListEntry):
        QUERY = "UPDATE list_entries SET list_id = ?, entry_text = ?, done = ? WHERE id = ?"
        params = (list_entry.list_id,list_entry.entry_text,list_entry.done,list_entry.id)
        executeQuery(self.db_path,QUERY,params=params)
    

    def updateAll(self,list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.update(list_entry)

    def delete(self,list_entry:ListEntryModule.ListEntry):
        QUERY = "DELETE FROM list_entries WHERE id = :id"
        params = {
            "id":list_entry.id
        }
        executeQuery(self.db_path,QUERY,params=params)
    

    def deleteAll(self,list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.delete(list_entry)

    def getById(self,id):

       QUERY = "SELECT * FROM list_entries WHERE id = :id"
       return executeQuery(self.db_path,QUERY,{"id":id},True)[0]

    def getByName(self,name):

        QUERY = "SELECT * FROM list_entries WHERE name = :name"
        return executeQuery(self.db_path,QUERY,{"name":name},True)[0]

    def getAll(self):
        
        QUERY = "SELECT * FROM list_entries"
        return executeQuery(self.db_path,QUERY,{},True)

