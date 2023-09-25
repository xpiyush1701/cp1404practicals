MENU = """G - Get valid score (0-100 inclusive)
P - Print result
S - Show stars
Q - Quit"""


def main():
    get_valid_score()
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
    print("Farewell.")


def get_valid_score():
    """
    Find a score between 0-100 inclusive.
    """
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
        return score


def print_result(score):
    """
    Print result based on score.
    """
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    """
    Print number of stars based on score.
    """
    print("*" * score)


main()
