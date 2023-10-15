"""
Estimate: 30 Minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    data = get_sorted_data(FILENAME)
    champion_to_count, countries = process_records(data)
    print_data(champion_to_count, countries)


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
    """Create dictionary of champions and set of countries from records (nested lists)."""
    champion_to_count = {}
    countries = set()
    for datum in data:
        countries.add(datum[1])  # Index of country
        try:
            champion_to_count[datum[2]] += 1  # Index of champion
        except KeyError:
            champion_to_count[datum[2]] = 1  # Index of champion
    return champion_to_count, countries


def print_data(champ_to_count, countries):
    """Display champions wins and countries."""
    print("Wimbledon Champions")
    for champ, count in champ_to_count.items():
        print(champ, count)
    print(f"These are the {len(countries)} countries that have won Wimbledon:")
    print(", ".join(country for country in countries))


main()
