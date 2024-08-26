# Level Up
# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    target = 50
    for x in range(5):
        if (x == 4):
            print('Last chance!')
        guess = input('Guess a number within the range of 1 to 100 ')
        if (int(guess) > 100 or int(guess) < 0):
            print('Value not within range, one chance used up!')
        elif (int(guess) == target):
            print('Congratulations, you guessed correctly!')
            break
        elif (x == 4):
            print('Sorry, you failed to guess the number in five attempts.')
        elif ((int(guess) - target) < 0):
            print('Your guess is too low!')
        elif ((int(guess) - target) > 0):
            print('Your guess is too high!')
        else:
            print('Incorrect input, one chance used up!')


# Call the function
guess_number()