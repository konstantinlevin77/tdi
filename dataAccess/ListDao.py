import sqlite3
import importlib.util as iutil

from executeQuery import executeQuery

# Annoying, I know 
todolist_spec = iutil.spec_from_file_location("TodoList","/home/konstantinlevin/Development/tdi/entities/TodoList.py")
TodoListModule = iutil.module_from_spec(todolist_spec)
todolist_spec.loader.exec_module(TodoListModule)


class ListDao():
    def __init__(self, db_path):
        self.db_path = db_path


    def add(self,todo_list):

        QUERY = "INSERT INTO lists(name,password) VALUES(?,?)"
        executeQuery(self.db_path,QUERY,(todo_list.name,todo_list.password))

    def addAll(self,todo_lists):

        for todo_list in todo_lists:
            self.add(todo_list)


    def update(self,todo_list):

        QUERY = "UPDATE lists SET name = ?, password = ? WHERE id = ?"
        executeQuery(self.db_path,QUERY,(todo_list.name,todo_list.password,todo_list.id))

    def updateAll(self,todo_lists):

        for todo_list in todo_lists:
            self.update(todo_list)            

    def delete(self,todo_list):

        QUERY = "DELETE FROM lists WHERE id = :id"
        executeQuery(self.db_path,QUERY,{"id":todo_list.id})

    def deleteAll(self,todo_lists):
        
        for todo_list in todo_lists:
            self.delete(todo_list) 

    def getById(self,id):

       QUERY = "SELECT * FROM lists WHERE id = :id"
       return executeQuery(self.db_path,QUERY,{"id":id},True)[0]

    def getByName(self,name):

        QUERY = "SELECT * FROM lists WHERE name = :name"
        return executeQuery(self.db_path,QUERY,{"name":name},True)[0]

    def getAll(self):
        
        QUERY = "SELECT * FROM lists"
        return executeQuery(self.db_path,QUERY,{},True)

