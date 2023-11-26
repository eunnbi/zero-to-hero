from crud import add_todo, get_todo_list, toggle_todo_done, delete_todo
from model import Todo


def main():
    todo_list = get_todo_list()
    print("***** Welcome Todo List *****")
    while True:
        print_menu()
        menu_num = get_menu_input()
        match menu_num:
            case 1:
                print_todo_list(todo_list)
            case 2:
                title = input("Title: ")
                content = input("Content: ")
                add_todo(todo_list, title, content)
            case 3:
                todo_id = input("Enter the ID of todo you want to delete: ")
                delete_todo(todo_list, todo_id)
            case 4:
                todo_id = input("Enter the ID of todo you want to toggle done status: ")
                toggle_todo_done(todo_list, todo_id)
            case 5:
                break
            case _:
                print("Please enter the valid number (1 ~ 5)")


def print_menu():
    print("\n*** Menu ***")
    print("1. Show Todo List")
    print("2. Add Todo")
    print("3. Delete Todo")
    print("4. Toggle Done Status")
    print("5. Quit")


def get_menu_input():
    while True:
        try:
            menu_num = int(input("Enter the menu number: "))
            return menu_num
        except ValueError:
            print("Please enter only number")


def print_todo_list(todo_list: dict[str, Todo]):
    print("\n*** Your Todo List ***")
    if len(todo_list) == 0:
        print("There's no todo list\n")
    else:
        for todo in todo_list.values():
            todo.print_todo()
            print('')


if __name__ == '__main__':
    main()
