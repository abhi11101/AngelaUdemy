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

player = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor\n"))
values = [rock, paper, scissors]
print(values[player])

comp = random.choice(values)
print(comp)

if comp == values[player]:
    print("Draw")
elif comp == rock and player == 1:
    print("You win")
elif comp == scissors and player == 0:
    print("You Win")
elif comp == paper and player == 2:
    print("You Win")
else:
    print("You Lose")

