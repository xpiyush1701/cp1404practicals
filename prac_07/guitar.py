"""
Estimated Time: 35 Minutes
Actual Time: 22 Minutes
"""
import csv

from prac_06.guitar_test import present_year


class Guitar:
    """Represent information about guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Give values regarding Guitar information"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a user-friendly string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, present_year):
        """Get Guitar age."""
        return present_year - self.year

    def is_vintage(self, present_year):
        """Check to see if Guitar is vintage."""
        return self.get_age(present_year) >= 50


# Create a list to store Guitar objects
guitars = []

# Read each line of guitars.csv
with open('guitars.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[0]
        year = int(row[1])
        cost = float(row[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

# Display the guitars using a loop
for guitar in guitars:
    print(guitar)
    age = guitar.get_age(present_year)
    if guitar.is_vintage(present_year):
        print(f"This guitar is {age} years old and is considered vintage.")
    else:
        print(f"This guitar is {age} years old and is not vintage.")
