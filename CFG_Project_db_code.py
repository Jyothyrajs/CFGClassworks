import mysql.connector
from config import HOST,USER,PASSWORD


class DbConnectionError(Exception):
    pass
#  python to  mysql connection
mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD)


def connect_db(db_name):
    context = mysql.connector.connect(host=HOST,
                                      user=USER,
                                      password=PASSWORD,
                                      database=db_name)
    return context

def insert_new_task(task):
    try:
        project_db = connect_db('Productivity')
        for item in task:
            # print(item.Task)
            query = f"INSERT INTO TODO_LIST(Task,Priority,No_hrs) VALUES('{item.Task}','{item.Priority}','{item.No_hrs}')"
            my_cursor = project_db.cursor()
            my_cursor.execute(query)
            print("Inserted")

    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()


def get_tasks():
    try:
        print("Retreiving")
        project_db = connect_db('Productivity')
        query = "SELECT Task FROM TODO_LIST"
        my_cursor = project_db.cursor()
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        for r in result:
            print(r)
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if project_db:
            project_db.close()

from collections import namedtuple
import csv

todolist_tpl = namedtuple('ToDoList_details','Task,Priority,No_hrs')
todo_list = map(todolist_tpl._make,csv.reader(open('todolist.csv','r')))
# for item in todo_list:
#     print(item.Task)

insert_new_task(todo_list)
get_tasks()