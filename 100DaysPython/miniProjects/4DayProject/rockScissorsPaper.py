import random


# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissors]

choice = int(input("What do you choose?\n Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"Your chose : {choice}")
print(game[choice])

print()
print("----------------------------------------------------------------------")
print()

random_choice = random.randint(0, 2)
print(f"Computer chose: {random_choice}")
print(game[random_choice])

if choice >= 0 or choice < 0:
    print("You typed an invalid number. You lose!")
elif choice == 0 and random_choice == 2:
    print("You win!")
elif random_choice == 0 and choice == 2:
    print("You lose!")
elif random_choice > choice:
    print("You lose!")
elif choice > random_choice:
    print("You win!")
elif random_choice == choice:
    print("It is a draw!")

