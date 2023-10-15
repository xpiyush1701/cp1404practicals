"""
Estimate: 20 Minutes
Actual:
"""


def main():
    """Main function"""
    name_to_email = {}
    email = input("Enter email address: ")
    while email != "":
        name = get_name_from_email(email)
        print(name)


def get_name_from_email(email):
    """Estimate and store name from emails"""
    prefix = email.split('@')[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name

main()
