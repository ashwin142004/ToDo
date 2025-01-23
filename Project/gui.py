import functions
import FreeSimpleGUI as fsg
import time 

fsg.theme("DarkAmber")

clock = fsg.Text('', key = "clock") 
label = fsg.Text("Type in a new todo:")
input = fsg.InputText(tooltip="Type in a new todo", key = "todo")
add_button = fsg.Button("Add", tooltip="Add a new todo")
list_box = fsg.Listbox(values = functions.get_todos(), key = "todos", enable_events=True ,size = (40, 10))
edit_button = fsg.Button("Edit", tooltip="Edit a todo")
complete_button = fsg.Button("Complete", tooltip="Completed a todo")
exit_button = fsg.Button("Exit", tooltip="Exit the program")

window = fsg.Window(
    "Todo List", 
    layout=[
        [clock],
        [label], 
        [input, add_button], 
        [list_box, edit_button, complete_button],
        [exit_button]], 
    font = ('Helvetica', 15)
    )

while True:
    event, values = window.read(timeout = 300)
    window["clock"].update(value = time.strftime("%d %b %Y, %H:%M:%S"))
 
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values = todos)
            window["todo"].update(value = "")   
        
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")
            
            except IndexError:
                fsg.popup("No todo selected")
        
        case "Complete":
            try:
                todo_to_remove = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window["todos"].update(values = todos)
                window["todo"].update(value = "")
            
            except IndexError:
                fsg.popup("No todo selected")
        
        case "Exit":
            break

        case "todos":
            window["todo"].update(value = values["todos"][0])

        case fsg.WIN_CLOSED:
            break

window.close()
