import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a new todo:")
input = fsg.InputText(tooltip="Type in a new todo", key = "todo")
add_button = fsg.Button("Add", tooltip="Add a new todo")
list_box = fsg.Listbox(values = functions.get_todos(), key = "todos", enable_events=True ,size = (40, 10))
edit_button = fsg.Button("Edit", tooltip="Edit a todo")
#delete_button = fsg.Button("Delete", tooltip="Delete a todo")

window = fsg.Window(
    "Todo List", 
    layout=[[label], [input, add_button], [list_box, edit_button]], 
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
            window["todos"].update(values = todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values = todos)
            except IndexError:
                fsg.popup("No todo selected")
        case "todos":
            window["todo"].update(value = values["todos"][0])

        case fsg.WIN_CLOSED:
            break

window.close()
