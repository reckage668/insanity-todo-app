FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-do item list to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# not working because name difference, or other reason?
if __name__ == "__main__":
    print("Hello!")
    print(get_todos())

#print("functions loaded.")
