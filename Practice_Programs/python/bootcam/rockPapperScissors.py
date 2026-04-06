import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = input("What do you do choose Press 1 for 'Rock', 2 for 'Paper', or 3 for 'Scissors'? \n")

RPS = ["rock", "paper", "scissors"]
computer_choice = random.randint(1, len(RPS))
# print(computer_choice)
if user_choice == '1':
    if computer_choice == 1:
        print(f"Your choice:\n {rock}")
        print(f"computer choice:\n {rock}")
        print("Its a Tie")
    elif computer_choice == 2:
        print(f"Your choice:\n {rock}")
        print(f"computer choice:\n {paper}")
        print("You Lost!")
    elif computer_choice == 3:
        print(f"Your choice:\n {rock}")
        print(f"computer choice:\n {scissors}")
        print("You Won!")

elif user_choice == '2':
    if computer_choice == 1:
        print(f"Your choice:\n {paper}")
        print(f"computer choice:\n {rock}")
        print("You Won!")
    elif computer_choice == 2:
        print(f"Your choice:\n {paper}")
        print(f"computer choice:\n {paper}")
        print("Its a Tie!")
    elif computer_choice == 3:
        print(f"Your choice:\n {paper}")
        print(f"computer choice:\n {scissors}")
        print("You Lost!")
elif user_choice == '3':
    if computer_choice == 1:
        print(f"Your choice:\n {scissors}")
        print(f"computer choice:\n {rock}")
        print("You Lost!")
    elif computer_choice == 2:
        print(f"Your choice:\n {scissors}")
        print(f"computer choice:\n {paper}")
        print("You Won!")
    elif computer_choice == 3:
        print(f"Your choice:\n {scissors}")
        print(f"computer choice:\n {scissors}")
        print("Its a Tie!")




