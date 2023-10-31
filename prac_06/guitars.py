"""
Estimated Time: 15 Minutes
Actual Time:
"""

from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitar_number = 1

    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))

    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{name} ({year}) : ${cost:.2f} added.")
    guitar_number += 1

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_status = " (vintage)" if guitar.is_vintage(2022) else ""
        print(vintage_status)


main()
