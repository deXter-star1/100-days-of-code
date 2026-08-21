import random

rock = """"
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

rpc = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if 0 <= user_choice <= 2:
    print(rpc[user_choice])

comp_choice = random.randint(0,2)
print("Computer Chose:")
print (rpc[comp_choice])

if user_choice == comp_choice:
    print("It's a draw!")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid Input. You Lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif user_choice == 2  and comp_choice == 0:
    print("You Lose!")
elif comp_choice > user_choice:
    print("You Lose!")
elif comp_choice < user_choice:
    print("You Win!")






