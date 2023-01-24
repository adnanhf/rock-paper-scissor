rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as rd

man_input = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
man_input = int(man_input)

comp_input = rd.randint(0, 2)

print("You choose:")
if man_input == 0:
  print(rock)
elif man_input == 1:
  print(paper)
elif man_input == 2:
  print(scissors)

print("Computer choose:")
if comp_input == 0:
  print(rock)
elif comp_input == 1:
  print(paper)
elif comp_input == 2:
  print(scissors)

if man_input == 0 and comp_input == 0:
  print("it's a draw!")
elif man_input == 0 and comp_input == 1:
  print("You lose")
elif man_input == 0 and comp_input == 2:
  print("You win")
elif man_input == 1 and comp_input == 0:
  print("You win")
elif man_input == 1 and comp_input == 1:
  print("it's a draw!")
elif man_input == 1 and comp_input == 2:
  print("You lose")
elif man_input == 2 and comp_input == 0:
  print("You lose")
elif man_input == 2 and comp_input == 1:
  print("You win")
elif man_input == 2 and comp_input == 2:
  print("it's a draw!")
