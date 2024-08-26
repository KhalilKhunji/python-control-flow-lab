# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input('Enter the month of the year (Jan - Dec) ')
    day = input('Enter the day of the month: ')
    from datetime import datetime
    from datetime import date
    currentdate = datetime.strptime(month + day, '%b%d').date()
    springstart = date(1900, 3, 20)
    springend = date(1900, 6, 20)
    summerstart = date(1900, 6, 21)
    summerend = date(1900, 9, 21)
    fallstart = date(1900, 9, 22)
    fallend = date(1900, 12, 20)
    winterstart = date(1900, 12, 21)
    winterend = date(1900, 3, 19)
    if (springstart <= currentdate <= springend):
        print(f'{month} {day} is in spring')
    elif (summerstart <= currentdate <= summerend):
        print(f'{month} {day} is in summer')
    elif (fallstart <= currentdate <= fallend):
        print(f'{month} {day} is in fall')
    elif (currentdate >= winterstart or currentdate <= winterend):
        print(f'{month} {day} is in winter')
    else:
        print('Erroneous entry')


# Call the function
determine_season()