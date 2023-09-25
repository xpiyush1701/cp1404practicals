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

MENU = """G - Get valid score (0-100 inclusive)
P - Print result
S - Show stars
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            get_valid_score()
        elif choice == "P":
            print_result()
        elif choice == "S":
            show_stars()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def print_result():
    pass


def show_stars():
    print("*" * score)


main()
