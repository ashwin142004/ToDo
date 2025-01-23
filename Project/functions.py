FILEPATH = "D:\\ToDo\\Project\\todos.txt"

def get_todos(filepath = FILEPATH):
    """Reads the todos from a file and returns a list of todos"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath = FILEPATH):
    """Writes the todos to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos)