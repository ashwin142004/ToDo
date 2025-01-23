import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a new todo:")
input = fsg.InputText(tooltip="Type in a new todo", key = "todo")
add_button = fsg.Button("Add", tooltip="Add a new todo")

window = fsg.Window(
    "Todo List", 
    layout=[[label], [input, add_button]], 
    font = ('Helvetica', 15)
    )

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WIN_CLOSED:
            break

window.close()
