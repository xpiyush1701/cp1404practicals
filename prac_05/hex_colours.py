COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Amaranth": "#e52b50", "Amethyst": "#9966cc",
                  "Aqua": "#00ffff", "Aquamarine2": "#76eec6", "Asparagus": "#87a96b", "Bittersweet": "#fe6f5e",
                  "Blond": "#faf0be", "Bright Cerulean": "#1dacd6"}

print(COLOUR_TO_CODE)

for colour in COLOUR_TO_CODE:
    print(f"{colour:3} is {COLOUR_TO_CODE[colour]}")

is_valid_colour = ""
while not is_valid_colour:
    try:
        colour_name = input("Colour Name: ").title()
        while colour_name != "":
            if colour_name in COLOUR_TO_CODE:
                colour_name = input("Colour Name: ").title()
        is_valid_colour = False
    except KeyError:
        print("Not a valid name")
