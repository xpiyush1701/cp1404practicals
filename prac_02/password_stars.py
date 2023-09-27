def main():
    min_length = 8

    password = get_password(min_length)
    print_asterisks(password)


def get_password(min_length):
    """Get a valid password that fulfills the minimum length of 8"""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long!")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print the number of "*" based on characters of the valid password."""
    print("*" * len(password))


main()
