'''
Refer this flow chart : Practice_Programs/python/docs/Treasure_island_flowchart.png
'''

print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("\nWelcome to Treasure Island. Your mission is to find the treasure. ")
print("your mission is to find the treasure. ")
print("You are at a cross road, where do you want to go? type 'left' or type 'right'.\n")
choice1 = input().lower()
if choice1 == 'left':
    print("You arrive at the the lake. ")
    print(" Need to cross the lake. You want to 'swim' or 'wait' for the boat")
    choice2 = input().lower()
    if choice2 == 'wait':
        print("You arrive at the other side of the lake. Great Job! ")
        print("Now You have got Three doors in Front of you! Which door would you like to go? 'red', 'yellow' or 'blue'? ")
        choice3 = input().lower()
        if choice3 == 'yellow':
            print("Congratulations You Win!! You have found the treasure. ")
        elif choice3 == 'blue':
            print("Eaten by Beast. Game Over!!")
        elif choice3 == 'red':
            print("Burned By Fire. Game Over!! ")
    else:
        print("Attacked by Trout ! Game Over")
else:
    print("Fall into a hole :( Game Over!! ")




