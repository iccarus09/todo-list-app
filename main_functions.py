import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, 'todolist.txt')
delete_filepath = os.path.join(BASE_DIR, 'deletelist.txt')

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)

def get_deletes(filepath=delete_filepath):
    with open(filepath, 'r') as file_local:
        deletes_local = file_local.readlines()
        return deletes_local

def write_deletes(delete_arg, filepath=delete_filepath):
    with open(filepath, 'w') as file_local:
        file_local.writelines(delete_arg)