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

rps = [rock, paper, scissors]

computer_choice = random.randint(0,2)

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

print(rps[int(user_choice)])

print(f"Computer chose:\n{rps[computer_choice]}")

if int(user_choice) == computer_choice :
    print("It's a draw!")
elif int(user_choice) > computer_choice :
    if int(user_choice) == 2 and computer_choice == 0 :
        print("You lose.")
    else:
        print("You Win!")
elif int(user_choice) == 0 and computer_choice == 2 :
    print("You Win!")
else:
    print("You lose.")
