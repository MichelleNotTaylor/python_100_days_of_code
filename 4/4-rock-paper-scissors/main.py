import random

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

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
computer_input = random.randint(0, 2)

if(user_input == "0"):
  print(rock)
elif(user_input == "1"):
  print(paper)
elif(user_input == "2"):
  print(scissors)

print("\nComputer chose:\n")
if(computer_input == 0):
  print(rock)
  if user_input == "0":
    print("\nTie.")
  if user_input == "1":
    print("\nYou win.")
  elif user_input == "2":
    print("\nYou lose.")
elif(computer_input == 1):
  print(paper)
  if user_input == "0":
    print("\nYou lose.")
  if user_input == "1":
    print("\nTie.")
  elif user_input == "2":
    print("\nYou win.")
elif(computer_input == 2):
  print(scissors)
  if user_input == "0":
    print("\nYou win.")
  if user_input == "1":
    print("\nYou lose.")
  elif user_input == "2":
    print("\nTie.")
