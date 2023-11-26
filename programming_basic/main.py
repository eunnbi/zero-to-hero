def main():
    print_hello_world()
    while True:
        try:
            dan = int(input("Enter the dan: "))
            print_gugudan(dan)
            break
        except ValueError:
            print("Please enter only number")


def print_hello_world():
    print("Hello World")


def print_gugudan(dan):
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")


if __name__ == '__main__':
    main()
