"""
Estimated Time: 35 Minutes
Actual Time:
"""


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) - ${self.cost:.2f}"
