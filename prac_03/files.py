# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

# 2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as
# above) then prints, "Your name is Bob" (or whatever the name is in the file).
with open("name.txt", "r") as in_file:
    for line in in_file:
        print(f"Your name is {line}")

# 3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the
# result, which should be... 59.
numbers = []
with open("numbers.txt", "r") as in_file:
    for number in in_file:
        number = number.strip()
        number = int(number)
        numbers.append(number)
    number_sum = numbers[0] + numbers[1]
    print(number_sum)

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number
# of numbers.
numbers = []
with open("numbers.txt", "r") as in_file:
    for number in in_file:
        number = number.strip()
        number = int(number)
        numbers.append(number)
    number_sum = sum(numbers)
    print(number_sum)
