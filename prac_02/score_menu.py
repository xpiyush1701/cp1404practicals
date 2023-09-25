"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
        choice = input(">>> ").upper()
        while choice != "Q":
            if choice == "C":
                convert_celsius_to_fahrenheit()
            elif choice == "F":
                convert_fahrenheit_to_celsius()
            else:
                print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
        print("Thank you.")


main()