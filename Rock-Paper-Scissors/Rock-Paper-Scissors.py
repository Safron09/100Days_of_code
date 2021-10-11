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
import random
player = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors ")
int_player = int(player)
computer = [rock, paper, scissors]
random_choice = random.choice(computer)
rock = new_rock = 0
paper = new_paper = 1
scissors = new_scissors = 2
new_computer = [new_rock, new_paper, new_scissors]
new_random_choice = random.choice(new_computer)

if int_player == 0 and new_random_choice == 0:
  print(computer[0])
  print(computer[0])
  print("ITs a Draw")
elif int_player == 1 and new_random_choice == 1:
  print(computer[1])
  print(computer[1])
  print("ITs a Draw")
elif int_player == 2 and new_random_choice == 2:
  print(computer[2])
  print(computer[2])
  print("ITs a Draw")
elif int_player == 1 and new_random_choice == 0:
  print(computer[1])
  print(computer[0])
  print("Computer won")
elif int_player == 1 and new_random_choice == 2:
  print(computer[1])
  print(computer[2])
  print("Player Lost")
elif int_player == 2 and new_random_choice == 0:
  print(computer[2])
  print(computer[0])
  print("Computer won")
elif int_player == 2 and new_random_choice == 1:
  print(computer[2])
  print(computer[1])
  print("Player Won")
elif int_player == 0 and new_random_choice == 1:
  print(computer[0])
  print(computer[1])
  print("Computer Won")
elif int_player == 0 and new_random_choice == 2:
  print(computer[0])
  print(computer[2])
  print("Player Won")
else:
  print("Wrong input, you lose")


