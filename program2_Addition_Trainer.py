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


def input_validation(user_input):
    if user_input != "":
        try:
            user_input = int(user_input)
            return user_input
        
        except ValueError:
            print("\nError. Invalid input.\n")
            return False
    else:
        print("Empty input is invalid.\n")
        return False

def quiz_proper():
    score = 0
    for question_number in range(1, 11):
        num_first, num_second = generate_number()
        answer1 = input(f"{question_number}.)  {num_first} + {num_second} = ")
        answer = input_validation(answer1)
        while answer == False:
            answer = 0
            trials = 0
            print("Note: You only have 3 attempts to correct your answer.")
            for trials in range(1, 4):
                if 0 < trials < 4:
                    print(f"Attempt No. {trials}")
                    answer1 = input(f"{question_number}.)  {num_first} + {num_second} = ")
                    answer = input_validation(answer1)
                    correct_answer = num_first + num_second
                    if answer != False:
                        break
            
                    if trials == 3:
                        print("Sorry. Game is terminated due to multiple unnecessary/invalid inputs.")
                        return False 
                else:
                    break
                
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
if current_score != False:
    final_rating = score_computation(current_score)
    print(f"Total score:    {final_rating}")
