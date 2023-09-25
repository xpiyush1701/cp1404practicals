def main():
    min_length = 8

    get_password(min_length)


def get_password(min_length):
    """
    Get a valid password that fulfills the minimum length of 8
    """
    while True:
        password = input("Enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long!")
        else:
            print_asterisks(password)
            break


def print_asterisks(password):
    """
    Print the number of "*" based on characters of the valid password.
    """
    print("*" * len(password))


main()
