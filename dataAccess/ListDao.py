import sqlite3
import importlib.util as iutil

# Annoying, I know 
todolist_spec = iutil.spec_from_file_location("TodoList","/home/konstantinlevin/Development/tdi/entities/TodoList.py")
TodoListModule = iutil.module_from_spec(todolist_spec)
todolist_spec.loader.exec_module(TodoListModule)

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
       result =  executeQuery(self.db_path,QUERY,{"id":id},True)

       if len(result) > 0:
           result = result[0]
       else:
           # id, name, password
           result = [None,None,None]

       return TodoListModule.TodoList(result[1],result[2],id=result[0])

    def getByName(self,name):

        QUERY = "SELECT * FROM lists WHERE name = :name"
        result =  executeQuery(self.db_path,QUERY,{"name":name},True)

        if len(result) > 0:
            result = result[0]
        else:
            result = [None,None,None]

        return TodoListModule.TodoList(result[1],result[2],id=result[0])

    def getAll(self):
        
        QUERY = "SELECT * FROM lists"
        result =  executeQuery(self.db_path,QUERY,{},True)
        result_in_entity_format = []

        for result_sample in result:
            result_in_entity_format.append(TodoListModule.TodoList(result_sample[1],result_sample[2],id=result_sample[0]))
        
        return result_in_entity_format

