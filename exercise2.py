# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = input('Please enter your age: ')
    try:
        age = int(age)
        VOTING_AGE = 18
        if age >= VOTING_AGE:
            print('You are eligible to vote!')
        elif age < 0:
            print('Impossible age')
        else:
            print('You are too young to vote!')
    except ValueError:
        print('Invalid input. Please enter a positive integer')
# Call the function
check_voting_eligibility()

# Checked Python documentation for error handling, not sure if other method for validation