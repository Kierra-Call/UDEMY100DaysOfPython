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

import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
comp_choice = random.randint(0,2)
#number_choice - 1







if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  options = [rock, paper, scissors]
  game_images = [rock, paper, scissors]
  user_image = game_images[user_choice]
  comp_image = game_images[comp_choice]
  print("You chose:")
  print(user_image)
  print("Computer chose:")
  print(comp_image)
 
  if user_choice == 0 and comp_choice == 2:
    print("You Win!")
  elif comp_choice > user_choice:
    print("You Lose")
  elif comp_choice == user_choice:
    print("It's a draw")
  elif user_choice == 2 and comp_choice == 0:
    print("You Lose")
  elif user_choice > comp_choice:
    print("You Win!")
