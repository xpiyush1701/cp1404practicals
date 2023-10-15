"""
Estimate: 30 Minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = get_sorted_data(FILENAME)
    champion_to_count = process_records()
    countries = process_data()
    print_data()


def get_sorted_data(filename):
    """Get data in nested lists form."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            datum = line.strip().split(",")
            data.append(datum)
    return data


def process_data():
    pass
    return data


def print_data():
    pass


main()
