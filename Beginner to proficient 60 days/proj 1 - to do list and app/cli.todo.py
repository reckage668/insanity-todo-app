# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%H:%M:%S %d%b%Y")
print("It is", now)

while True:
    user_action = input("Add, show, change, completed, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith('change'):
        try:
            number = int(user_action[7:])
            print(number)

            number = number - 1

#            todos = get_todos()
            todos = functions.get_todos()

            new_todo = input("enter the new task: ")
            todos[number] = new_todo + "\n"

#            write_todos(todos)
            functions.write_todos(todos)

        except ValueError:
            print("Command invalid, 'change #' only please.")
            continue

    elif user_action.startswith('completed'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"To do '{todo_to_remove}' is now complete."
            print(message)
        except IndexError:
            print("Invalid item number, Try again.")
            continue

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}. {item}"
            print(row)

    elif 'exit' in user_action:
        break
    else:
        print("uh, what?")

print("Bye!")
