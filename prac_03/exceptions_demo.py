"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If the user inputs are not integers, a ValueError will occur.
2. When will a ZeroDivisionError occur?
If the denominator input is 0, a ZeroDivisionError will occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by adding an error checking program that does not allow an input
of 0 for the denominator.
"""
is_valid_input = False
while not is_valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero!")

        fraction = numerator / denominator
        print(fraction)
        print("Finished.")

        break

    except ValueError:
        print("Numerator/denominator must be valid numbers!")

    except ZeroDivisionError:
        print("Cannot divide by zero!")
