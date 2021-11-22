# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def get_input():
    first_input = input("Good day!\n\nEnter first number: ")
    second_input = input("Enter second number: ")
    third_input = input("Enter third number: ")
    fourth_input = input("Enter fourth number: ")
    return first_input, second_input, third_input, fourth_input


def input_validation(first_try, second_try, third_try, fourth_try):
    if (first_try != "") and (second_try != "") and (third_try != "") and (fourth_try != ""):
        try:
            first_int, second_int, third_int, fourth_int = float(
                first_try), float(second_try), float(third_try), float(fourth_try)
            if (first_int - int(first_int) == 0):
                first_int = int(first_int)

            if (second_int - int(second_int) == 0):
                second_int = int(second_int)

            if (third_int - int(third_int) == 0):
                third_int = int(third_int)
            
            if (fourth_int - int(fourth_int) == 0):
                fourth_int = int(fourth_int)

            return first_int, second_int, third_int, fourth_int

        except ValueError:
            print("\nError. Please enter numbers.")
            return False, False, False, False
    else:
        print("\nEmpty input is invalid. Please try again.")
        return False, False, False

first, second, third, fourth = get_input()
first_valid, second_valid, third_valid, fourth_valid = input_validation(first, second, third, fourth)
