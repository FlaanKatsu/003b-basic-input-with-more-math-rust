#!python3
"""
Assignment: Exchange rate
The current exchange rate is 1.25 CAD per 1 USD
Create a program that asks the user for the number of Canadian Dollars they have
and then have the program display how many USD that is equivalent to:
You may need to use rounding or decimal formatting


example
How many Canadian Dollars do you have? 10
That is worth $8.00 USD

How many Canadian Dollars do you have? 1.25
That is worth $1.00 USD
"""
input("this is a program that converts $ CAD to $ USD.")
C = float(input("please enter the amount of CAD you would like to convert to USD:"))
round(C, 2)
#R represents the exchange rate.
R = 1.25
U = C / R
u = round(U, 2)
print(f"{C} CAD is {u} in american dolars.")