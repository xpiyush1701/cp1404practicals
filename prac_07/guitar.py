"""
Estimated Time: 35 Minutes
Actual Time: 22 Minutes
"""


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
