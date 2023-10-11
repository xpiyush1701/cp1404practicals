"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# Loop that prints all the states and names neatly lined up with string formatting
for name in CODE_TO_NAME:
    print(f"{name:3} is {CODE_TO_NAME[name]}")

is_valid_input = False
while not is_valid_input:
    try:
        state_code = input("Enter short state: ").upper()
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            raise NameError
    except NameError:
        print("Not a valid name")
