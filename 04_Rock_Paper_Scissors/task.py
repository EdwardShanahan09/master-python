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

options = [rock, paper, scissors]
random_number = random.randint(0, 2)
computer_choice = random_number
user_choice = int(input("What do you? Type 0 for Rock, 1 for Paper or 2 for scissor."))
print(options[user_choice])
print("Computer Choice:")
print(options[computer_choice])

if(user_choice == computer_choice):
    print("Draw")
elif(user_choice == 0 and computer_choice == 2):
    print("You Win!")
elif(computer_choice == 0 and user_choice == 2):
    print("You Lose!")
elif(user_choice > user_choice):
    print("You Win")
elif(computer_choice > user_choice):
    print("You Lose!")
else:
    print("Please enter a valid option, You Lose!")


