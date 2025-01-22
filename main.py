todos = []
while True:
    user_action = input("Type add, edit, show, completed or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        
        todos.append(todo + '\n')
        
        with open("todos.txt", "w") as file:
            file.writelines(todos)
    
    elif user_action.startswith("show"):    
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1} - {todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:    
            todo_index = int(user_action[5:])
            todo_index -= 1
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            
            new_todo = input("Type the new todo text:")
            todos[todo_index] = new_todo + '\n'
            
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError | IndexError:
            print("Invalid index")
            continue
        
    elif user_action.startswith("complete"):
        try:
            todo_index = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = todo_index - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)  
        except ValueError | IndexError:
            print("Invalid index")
            continue

    elif user_action.startswith('exit'):
        print("Goodbye!")
        break
    else:
        print("Invalid command")
    