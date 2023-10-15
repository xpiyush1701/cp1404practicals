"""
Estimate: 30 Minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = get_sorted_data(FILENAME)
    champion_to_count, countries = process_records(data)
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


def process_records(data):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for datum in data:
        countries.add(datum[1])  # Index of country
        try:
            champion_to_count[datum[2]] += 1  # Index of champion
        except KeyError:
            champion_to_count[datum[2]] = 1  # Index of champion
    return champion_to_count, countries



def print_data():
    pass


main()
