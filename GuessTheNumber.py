import random
#Guess the number between 1-100 game

random_num = random.randint(1,100)

while True:
    try:
        try_input = int(input(f"Guess the number between 1-100\n"))
        if  random_num < try_input:
            print(f"You Entered {try_input} - Too High! Try Again")
        elif try_input < random_num:
            print(f"You Entered {try_input} - Too Low! Try Again")
        else:
            print(f"{try_input} Is Correct!\nYou Win!")
            break
    except ValueError:
            print("Sorry Must Enter Number Between 1-100")

