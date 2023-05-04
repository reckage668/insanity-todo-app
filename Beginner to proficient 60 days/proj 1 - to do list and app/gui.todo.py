import functions
import PySimpleGUI as sg
import time

sg.theme("DarkGreen 1")

# now = time.strftime("%H:%M:%S %d%b%Y")
clock = sg.Text('', key='clock')
label = sg.Text("Type in a task to do.")
input_box = sg.InputText(tooltip="Enter a to do", key="todo")
add_button = sg.Button(image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Task", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", mouseover_colors="LightBlue2",
                            tooltip="Complete a task.", key="Complete")
exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Garamond", 18))

while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%H:%M:%S %d%b%Y"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_change = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_change)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item to change first.", font=("Garamond", 16))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Select an item to complete first.", font=("Garamond", 16))
        case "todos":
            window['todo'].update(value= values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()
