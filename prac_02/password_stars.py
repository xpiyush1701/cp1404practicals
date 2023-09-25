min_length = 8

while True:
    password = input("Enter a password: ")
    if len(password) < min_length:
        print(f"Password must be at least {min_length} characters long!")
    else:
        print("*" * len(password))
        break
