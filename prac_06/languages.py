"""
Estimated Time: 15 Minutes
Actual Time: 26 Minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    programming_languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
