'''
Write a Tip Calculator
Inputs:
Welcome to the Tip Calculator!
What was your total bill?
How much tip would you like to give? 10, 12, or 15?
How many people to split the bill?
Each Person Should Pay:
'''

print("Welcome to the Tip Calculator! ")
bill = float(input("What was your total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))

amount_perPerson=float((bill+(bill*tip/100))/people)

print("Each Person Should Pay: $ ")
print(amount_perPerson)