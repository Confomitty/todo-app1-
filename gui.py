import time
import functions
import FreeSimpleGUI as fsg

fsg.theme("DarkTeal3")

clock = fsg.Text("" , key = 'clock')
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip = "Enter a to-do", key = "todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values = functions.get_todos(), key = "todos",     #values accepts only a list arg
                       enable_events = True,
                       size = (45,10) )
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window('My To-Do App' ,
                    layout = [[clock],
                              [label],
                              [input_box, add_button],
                              [list_box, edit_button],
                              [complete_button, exit_button]],
                    font = ('Bahnschrift' ,15))

while True :
    event , values = window.read(timeout = 1000)
    window['clock'].update(value = time.strftime("%d %B %Y %H:%M:%S"))
    print(event)
    print(values)
    match event :
        case "Add":
            todos = functions.get_todos()

            if values['todo'] == "":
                fsg.popup("Please enter a to-do" ,font = ("Bahnschrift", 10))

            else :
                new_todo = values['todo']
                todos.append(new_todo + '\n')
                functions.write_todos(todos)
                window['todos'].update(values = todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)

            except IndexError:
                fsg.popup("Please select an item first!", font = ('Bahnschrift', 10))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')

            except IndexError:
                fsg.popup("Please select an item first!", font = ('Bahnschrift', 10))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case fsg.WIN_CLOSED:
            break


window.close()
