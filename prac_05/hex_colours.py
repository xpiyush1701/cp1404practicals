COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Amaranth": "#e52b50", "Amethyst": "#9966cc",
                  "Aqua": "#00ffff", "Aquamarine2": "#76eec6", "Asparagus": "#87a96b", "Bittersweet": "#fe6f5e",
                  "Blond": "#faf0be", "Bright Cerulean": "#1dacd6"}

colour_name = input("Colour Name: ").title()
while colour_name != "":
    print(f"{colour_name} is {COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("Colour Name: ").title()
