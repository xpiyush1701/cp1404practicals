"""
CP1404/CP5632 - Practical
The general pattern of a menu-driven program
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").lower()
print("Finished.")
