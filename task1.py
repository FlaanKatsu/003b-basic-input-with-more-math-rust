#!python3

"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
import math

input("This program calculates compounding interest.(press enter)")
print('It uses the formula \"I=P*R*D/365\"')
print("where I = interest, P = principal, R = rate and D = days in the month. 365 is the amount of days in a year.")
P = int(input("Please enter the current amount of money you have (or wish to calculate) and press enter:"))
R = float(input("Now please enter the interest rate in percentage, using a value less than 1.00 (1.00 = 100%):"))
D = int(input("Now please enter the amount of days in the current month:"))
C = str(input("What currency are you using? Type it out and press enter:"))
i = P * R * D / 365
I = round(i, 2)
print(f"Your interest is {I} {C}.")