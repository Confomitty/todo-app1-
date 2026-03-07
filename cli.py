from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is: ", now)
while True :
    user_action = input("Type add, show, edit , complete or exit : ").strip().lower()


    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos(todos)


    elif user_action.startswith('show'):

        todos = get_todos()

    #  new_todos = [item.strip('\n') for item in todos]   list comprehension

        for index , item in enumerate(todos ,1):
            row = f"{index}-{item}"
            print(row,end ='')


    elif user_action.startswith('edit'):
        try :
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter the new todo : ")
            todos[number - 1] = new_todo + '\n'

            write_todos(todos, "todos.txt")


        except ValueError :
            print("The command is invalid.")
            continue

    elif user_action.startswith('complete') :
        try :
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos,"todos.txt")

            message = f"Todo {todos_to_remove} was removed."
            print(message)

        except ValueError :
            print("That item does not exist.")
            continue


    elif 'exit' in user_action :
        break


    else :
        print("Invalid command.")

print("Bye!")
