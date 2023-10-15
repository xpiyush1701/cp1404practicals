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
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        name_to_email[email] = name
        email = input("Email: ")

    for name, email in name_to_email.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Estimate and store name from emails"""
    prefix = email.split('@')[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name

main()
