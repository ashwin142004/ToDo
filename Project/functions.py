def get_todos(filepath = "todos.txt"):
    """Reads the todos from a file and returns a list of todos"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath = "todos.txt"):
    """Writes the todos to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos)