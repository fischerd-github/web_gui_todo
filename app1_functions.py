FILEPATH = "todos.txt"


def print_numbered_item_list(todos_arg):
    for index, item in enumerate(todos_arg):
        item = (item.title()).strip('\n')
        print(f"{index + 1}:  {item}")
    return


def get_todos(filepath_arg=FILEPATH):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath_arg, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ Write a to-do items list in a text file. """
    with open(filepath_arg, 'w') as file:
        file.writelines(todos_arg)


'''
print(__name__)
print("hello from app1_functions from outside the conditional")
'''
if __name__ == "__main__":
    print("Hello from inside the conditional within app1_functions.py")