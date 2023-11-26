from crud import add_todo, get_todo_list, toggle_todo_done, delete_todo
from database import get_db_connection, create_todo_list_table
from model import Todo


def main():
    conn = get_db_connection()
    create_todo_list_table(conn)
    print("***** Welcome Todo List *****")
    while True:
        print_menu()
        menu_num = get_int_input("Enter the menu number: ")
        match menu_num:
            case 1:
                todo_list = get_todo_list(conn)
                print_todo_list(todo_list)
            case 2:
                title = input("Title: ")
                content = input("Content: ")
                add_todo(conn, title, content)
            case 3:
                todo_id = get_int_input("Enter the ID of todo you want to delete: ")
                delete_todo(conn, todo_id)
            case 4:
                todo_id = get_int_input("Enter the ID of todo you want to toggle done status: ")
                toggle_todo_done(conn, todo_id)
            case 5:
                break
            case _:
                print("Please enter the valid number (1 ~ 5)")
    conn.close()


def print_menu():
    print("\n*** Menu ***")
    print("1. Show Todo List")
    print("2. Add Todo")
    print("3. Delete Todo")
    print("4. Toggle Done Status")
    print("5. Quit")


def get_int_input(message: str):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Please enter only number")


def print_todo_list(todo_list: list[Todo]):
    print("\n*** Your Todo List ***")
    if len(todo_list) == 0:
        print("There's no todo list\n")
    else:
        for todo in todo_list:
            todo.print_todo()
            print('')


if __name__ == '__main__':
    main()