'''
Small Pizza : $15
Medium, Pizza : $20
Large Pizza : $25

Add Pepperoni for small pizza(Y/N): $2
Add Pepperoni for medium or large pizza(Y/N): $3
Add extra cheeze for any pizza(Y/N): $1

Take your order and prepare final bill
'''
from xmlrpc.client import Boolean

print("Welcome to the Python Pizza Shop! ")
print("--------------------------------------")
print("Below is the Menu: \n")
print("1) Small Pizza: $15")
print("2) Medium, Pizza: $20")
print("3) Large Pizza: $25")
print("4) Add Pepperoni (for small pizza): $2")
print("5) Add Pepperoni (for medium or large pizza): $3")
print("6) Add extra cheeze for any pizza: $1\n")
print("--------------------------------------")
print("Please select the Pizza you want to order ----> \n")

# User Input for Orders
bill = 0
size = input("Which size would you like to order? S/M/L: ")
pepperoni = input("Do you want to add pepperoni? (Y/N): ? ")
cheeze = input("Do you want to add cheeze? (Y/N): ")

# User Input for Pizza
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("You have entered the wrong option. Please enter a valid size.")

# User Input for Pepperoni
if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# User Input for Extra Cheeze
if cheeze == 'Y':
    bill += 4

print(f"Total bill: ${bill}")
