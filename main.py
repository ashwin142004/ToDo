todos = []
while True:
    user_action = input("Type add, edit, show, completed or exit: ").strip()

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
            for index, todo in enumerate(todos):
                print(f"{index + 1} - {todo}")
        case "exit":
            print("Goodbye!")
            break
        case "completed" | "complete":
            todo_index = int(input("Type the number of the todo to mark as completed:"))
            todo_index -= 1
            todos.pop(todo_index)
        case _:
            print("Invalid action")