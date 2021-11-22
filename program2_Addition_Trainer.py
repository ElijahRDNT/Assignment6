# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random


def system_header():
    print("\nGood day! Welcome to Addition Trainer Quiz. \n\nLet's get started...\n")


def generate_number():
    first_number = random.randint(0, 99)
    second_number = random.randint(0, 99)
    return first_number, second_number


def quiz_proper():
    score = 0
    for question_number in range(1, 11):
        num_first, num_second = generate_number()
        answer = float(
            input(f"{question_number}.)  {num_first} + {num_second} = "))
        correct_answer = num_first + num_second
        if answer == correct_answer:
            print("Correct!\n")
            score = score + 1

        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

    return score


def score_computation(score_compute):
    item_numbers = 10
    final_score = str(f"{score_compute}\{item_numbers}")

    return final_score


system_header()
current_score = quiz_proper()
final_rating = score_computation(current_score)
print(f"Total score:    {final_rating}")
