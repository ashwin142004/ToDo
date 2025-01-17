todos = []
while True:
    user_action = input("Type add, edit, show or exit:").strip()

    match user_action:
        case "add":
            todo = input("Type your todo:")
            todos.append(todo)
        case "edit":   
            todo_index = int(input("Type the number of the todo to edit:"))
            todo_index -= 1
            new_todo = input("Type the new todo:")
            todos[todo_index] = new_todo
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid action")