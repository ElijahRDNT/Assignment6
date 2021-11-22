# Program 1: Number Sorter
# Create a program that ask 4 numbers.
# Print the 4 numbers from highest to lowest using only if-else statement.

def get_input():    # function to collect inputs
    first_input = input("Good day!\n\nEnter first number: ")
    second_input = input("Enter second number: ")
    third_input = input("Enter third number: ")
    fourth_input = input("Enter fourth number: ")
    return first_input, second_input, third_input, fourth_input


def input_validation(first_try, second_try, third_try, fourth_try):
    if (first_try != "") and (second_try != "") and (third_try != "") and (fourth_try != ""):   # if inputs are not empty, the program continues
        try:
            first_int, second_int, third_int, fourth_int = float(       # converts inputs into float datatype to enable inputs with decimal points
                first_try), float(second_try), float(third_try), float(fourth_try)
            if (first_int - int(first_int) == 0):   # if the input is a whole number, it will be converted into int datatype to flash the original input back if it is the lowest
                first_int = int(first_int)           # for example, without these codes, an input of 1 will be flashed as 1.0. But with this, input 1 will be flashed as 1

            if (second_int - int(second_int) == 0):
                second_int = int(second_int)

            if (third_int - int(third_int) == 0):
                third_int = int(third_int)

            if (fourth_int - int(fourth_int) == 0):
                fourth_int = int(fourth_int)

            return first_int, second_int, third_int, fourth_int

        except ValueError:
            print("\nError. Please enter numbers.") # inputs that can't be converted to float datatype is restricted
            return False, False, False, False
    else:
        print("\nEmpty input is invalid. Please try again.")    # restricts empty inputs
        return False, False, False
    # This time, negative inputs are allowed

def number_order(first_no, second_no, third_no, fourth_no): # this function is to classify the numbers from lowest to greatest value
    if first_no < second_no:        # this time, I tried to tdo the classifying by pairs of numbers or inputs
        small_first_pair = first_no
        high_first_pair = second_no
    else:
        small_first_pair = second_no
        high_first_pair = first_no

    if third_no < fourth_no:
        small_second_pair = third_no
        high_second_pair = fourth_no
    else:
        small_second_pair = fourth_no
        high_second_pair = third_no

    if small_first_pair < small_second_pair:
        least_num = small_first_pair
        mid_num_a = small_second_pair
    else:
        least_num = small_second_pair
        mid_num_a = small_first_pair

    if high_first_pair > high_second_pair:
        greatest_num = high_first_pair
        mid_num_b = high_second_pair
    else:
        greatest_num = high_second_pair
        mid_num_b = high_first_pair

    if mid_num_a < mid_num_b:
        return (least_num, mid_num_a, mid_num_b, greatest_num)
    else:
        return (least_num, mid_num_b, mid_num_a, greatest_num)


first, second, third, fourth = get_input()  # storing of inputs in different global variables
first_valid, second_valid, third_valid, fourth_valid = input_validation(
    first, second, third, fourth)
if (first_valid != False) and (second_valid != False) and (third_valid != False) and (fourth_valid != False):   # if the input_validation() function did not return a false value, the program proceeds
    least, lesser, greater, greatest = number_order(
        first_valid, second_valid, third_valid, fourth_valid)
    print(
        f"\nThe order of numbers from highest to lowest is:   {greatest}, {greater}, {lesser}, {least}")
