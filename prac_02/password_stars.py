def main():
    min_length = 8

    get_password(min_length)


def get_password(min_length):
    while True:
        password = input("Enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long!")
        else:
            print_asterisks(password)
            break


def print_asterisks(password):
    print("*" * len(password))


main()
