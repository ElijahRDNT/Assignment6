# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def get_input():
    first_input = input("Good day!\n\nEnter first number: ")
    second_input = input("Enter second number: ")
    third_input = input("Enter third number: ")
    fourth_input = input("Enter fourth number: ")
    return first_input, second_input, third_input, fourth_input


first, second, third, fourth = get_input()
