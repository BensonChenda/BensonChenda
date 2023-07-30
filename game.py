import random

def my_game():
    print("Welcome to Ben's game!!!")
    print("To proceed, Choose an option among(Rock, Paper or Scissors:)")
    your_choice = input().lower()

    option = ["rock","paper","scissors"]
    PCs_choice = random.choice(option)
    print(f"Computer chooses:  {PCs_choice}")

    if your_choice == PCs_choice:
        print("that's a tie, You've drawn!!!")
    elif (your_choice == "rock" and PCs_choice == "scissors") or (your_choice == "paper" and PCs_choice == "rock") or (your_choice == "scissors" and PCs_choice == "paper"):
            print("CONGRATULATIONS,YOU'VE WON")
    else:
        print("SORRY, YOU'VE LOST ")
my_game()
my_game()
my_game()
