from functions import get_todos, write_todos
import time

now = time.strftime("%H:%M:%S, %d %b %Y")
print(f"Current time: {now}")

while True:
    user_action = input("Type add, edit, show, completed or exit: ").strip()

    if user_action.startswith("add"): 
        todo = user_action[4:]
        
        todos = get_todos()
        
        todos.append(todo + '\n')

        write_todos(todos)        
    
    elif user_action.startswith("show"):    
        
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1} - {todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:    
            todo_index = int(user_action[5:])
            todo_index -= 1
            
            todos = get_todos()
            
            new_todo = input("Type the new todo text:")
            todos[todo_index] = new_todo + '\n'
            
            write_todos(todos)
        
        except ValueError:
            print("Invalid index")
            continue
        
        except IndexError:
            print("Invalid index")
            continue
        
    elif user_action.startswith("complete"):
        try:
            todo_index = int(user_action[9:])
            
            todos = get_todos()
            
            index = todo_index - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)  
        
        except ValueError:
            print("Invalid index")
            continue
        
        except IndexError:
            print("Invalid index")
            continue

    elif user_action.startswith('exit'):
        print("Goodbye!")
        break
    
    else:
        print("Invalid command")

