# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, out_file)
