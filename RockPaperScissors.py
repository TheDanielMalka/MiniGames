import random

# RockPaperScissors Game

while True:
    emojis = {"r": "🎱", "p": "📑", "s": "✂"}
    choices = ("r", "p", "s")
    user_choice = input("Rock, Paper, or Scissors? (r/p/s)\n").lower()
    try:
        computer_choice = random.choice(choices)
        print(f"You chose {emojis[user_choice]}\nComputer chose {emojis[computer_choice]}")
        if user_choice == computer_choice:
            print(f"Draw you both chose {emojis[user_choice]}")
        elif (user_choice == "r" and computer_choice == "s")\
            or (user_choice == "s" and computer_choice == "p")\
            or (user_choice == "p" and computer_choice == "r"):
            print(f"You Won With {emojis[user_choice]}")
        elif (computer_choice == "r" and user_choice == "s") \
            or (computer_choice == "s" and user_choice == "p") \
            or (computer_choice == "p" and user_choice == "r"):
            print(f"Computer Won With {emojis[computer_choice]}")
        try:
            exit_input = input("Do you want to play again? (y/n)\n").lower()
            if exit_input == "n":
                break
            elif exit_input == "y":
                print("Thank you for playing")
            elif exit_input != "n" or exit_input != "y":
                print("Invalid input")
                last_input = input("Do you want to play again? Last time before Shutdown (y/n)\n").lower()
                if last_input == "n":
                    break
                elif last_input == "y":
                    print("Thank you for playing")
                else:
                    break
        except ValueError:
            print("Invalid input")
    except KeyError:
        print("Invalid choice")
