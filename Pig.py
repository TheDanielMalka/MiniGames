import random


def roll_func():
    roll = random.randint(1,6)
    return roll


while True:
    players = input("Enter the number of players ( 2 - 4 ): \n")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be an integer between 2 and 4")
    else:
        print("Invalid input , if u want to play again run it again")


maximum = 50
player_score = [0 for _ in range(players)]


while max(player_score) < maximum:

    for turn_index in range (players):
        print(f"Board Score Status : {player_score} We play till 50! ")
        print(f"Player {turn_index+1} turn has started \nGood Luck !! ")
        print(f"Your total score is {player_score[turn_index]}")
        current_score = 0

        while True:
            roll_ask = input("Roll or pass ? ( r / p ) : \n")
            if roll_ask.lower() != "r":
                break

            player_turn = roll_func()
            if player_turn == 1:
                print("You rolled 1! Turn done!")
                break
            else:
                current_score += player_turn
                print(f"Your rolled {player_turn}!")

            print(f"Your current score is {current_score}")

        player_score[turn_index] += current_score
        print(f"Your score is now  {player_score[turn_index]}")



