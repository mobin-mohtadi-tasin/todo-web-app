def get_todos(filepath="todo.txt"):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local if todos_local else []


def write_todos(todos_arg,filepath="todo.txt"):
    with open(filepath, 'w') as file:
        file.writelines([todo if todo.endswith("\n") else todo + "\n" for todo in todos_arg])

if __name__ == "__main__":
    print("hello")
    print(get_todos())