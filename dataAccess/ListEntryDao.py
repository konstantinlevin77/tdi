import importlib.util as iutil
from os import EX_OSFILE
import sqlite3

list_entry_module_spec = iutil.spec_from_file_location("ListEntry", "/home/konstantinlevin/Development/tdi/entities/ListEntry.py")
ListEntryModule = iutil.module_from_spec(list_entry_module_spec)
list_entry_module_spec.loader.exec_module(ListEntryModule)


def executeQuery(db_path, query, params=None, select=False):

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute(query, params)
        if select:
            res = cursor.fetchall()
            connection.close()
            return res

        else:
            connection.commit()
            connection.close()


class ListEntryDao():

    def __init__(self, db_path):
        self.db_path = db_path

    def add(self, list_entry: ListEntryModule.ListEntry):
        QUERY = "INSERT INTO list_entries(list_id,entry_text,done) VALUES(?,?,?)"
        params = (list_entry.list_id, list_entry.entry_text, list_entry.done)
        executeQuery(self.db_path, QUERY, params=params)

    def addAll(self, list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.add(list_entry)

    def update(self, list_entry: ListEntryModule.ListEntry):
        QUERY = "UPDATE list_entries SET list_id = ?, entry_text = ?, done = ? WHERE id = ?"
        params = (list_entry.list_id, list_entry.entry_text,
                  list_entry.done, list_entry.id)
        executeQuery(self.db_path, QUERY, params=params)

    def updateAll(self, list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.update(list_entry)

    def delete(self, list_entry: ListEntryModule.ListEntry):
        QUERY = "DELETE FROM list_entries WHERE id = :id"
        params = {
            "id": list_entry.id
        }
        executeQuery(self.db_path, QUERY, params=params)

    def deleteAll(self, list_of_list_entries):
        for list_entry in list_of_list_entries:
            self.delete(list_entry)

    def deleteByListId(self, list_id):
        QUERY = "DELETE FROM list_entries WHERE list_id = :list_id"
        params = {
            "list_id": list_id
        }
        executeQuery(self.db_path, QUERY, params)

    def getById(self, id):

       QUERY = "SELECT * FROM list_entries WHERE id = :id"
       result = executeQuery(self.db_path, QUERY, {"id": id}, True)
       if (len(result)>0):
           result = result[0]
       else:
           # id, list_id, text_entry, done
           result = [None,None,None,None] 
       
       return ListEntryModule.ListEntry(result[1],result[2],result[3],id=result[0])

       
    
    def getByListId(self,list_id):
        QUERY = "SELECT * FROM list_entries WHERE list_id = :list_id"
        result =  executeQuery(self.db_path,QUERY,{"list_id":list_id},True)
        if len(result)>0:
            result_entity = []
            for r in result:
                result_entity.append(ListEntryModule.ListEntry(r[1],r[2],r[3],id=r[0]))
            return result_entity
        else:
            result = [None,None,None,None]
            return [ListEntryModule.ListEntry(result[1],result[2],result[3],id=result[0])]


    def getByName(self,name):

        QUERY = "SELECT * FROM list_entries WHERE name = :name"
        result = executeQuery(self.db_path,QUERY,{"name":name},True)

        if len(result) > 0:
            result = result[0]
        
        else:
            result = [None,None,None,None]

        return ListEntryModule.ListEntry(result[1],result[2],result[3],id=result[0])

    def getAll(self):
        
        QUERY = "SELECT * FROM list_entries"
        result = executeQuery(self.db_path,QUERY,{},True)
        result_in_entity_format = []
        for result_sample in result:
            result_in_entity_format.append(ListEntryModule.ListEntry(result_sample[1],result_sample[2],result_sample[3],id=result_sample[0]))

        return result_in_entity_format