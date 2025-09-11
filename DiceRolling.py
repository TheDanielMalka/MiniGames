import random
#DiceRolling

playing = True
while playing:
    print("Welcome to the Dice Rolling Game!")
    check = input("You wanna play? (y/n) \n").lower()
    if check == "y":
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        print(f"{first_dice} {second_dice}")
    elif check == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")
