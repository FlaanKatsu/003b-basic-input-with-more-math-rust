#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

#assignment error: the assignment instructions ask for 4 items, the example is 5 items.

#if 5 items are required, simply add E as a variable, and again add E to the bracked in line 28.

#testing chinese characters as variables
print("this program is a simple sales tax calculator.")
print("it will calculate the total tax of 4 items.")
A = float(input("please enter the price of the first item:"))
B = float(input("please enter the price of the second item:"))
C = float(input("please enter the price of the third item:"))
D = float(input("finally, please enter the price of the 4th item."))
本 = ( A + B + C + D )
中 = 本 * 0.12
本当 = round(中 + 本, 2)
日 = round(本, 2)
好 = round(中, 2)
print(f"the subtotal is {日}, the tax is {好} and the total is {本当}.")