"""
Estimated Time: 15 Minutes
Actual Time:
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        reflection_str = f"Reflection={self.reflection}"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"
