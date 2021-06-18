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