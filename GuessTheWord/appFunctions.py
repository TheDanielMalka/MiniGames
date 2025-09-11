import random

def main():
    word_check = random_word()
    guessed_letters = []
    while not validate_guess(word_check,guessed_letters):# שימוש כאן ב NOT כי רק במקרה שכל האותיות יושלמו יתקיים התנאי אחרת
        progress(word_check, guessed_letters) #                הלולאה תמשיך לרוץ עד לקאונטר שנקבע
        guess_input = input("\n" + "Guess a letter: \n").lower()

        if len(guess_input) != 1 or not guess_input.isalpha():
            print("Invalid input entered. Please try again with a single letter.")
            continue # אומר לך מפה לחזור לראש הלולאה מההתחלה

        if guess_input in guessed_letters:
            print("You guessed this letter already. Please try again with a single letter.!")
            continue

        guessed_letters.append(guess_input)

        if validate_guess(word_check,guessed_letters):
            print("You guessed the word correctly!")
            print("=" * 40)
            print("The word was: " + word_check)
            print("=" * 40)
            restart_game = input("Do you want to play again? (y/n): \n").lower()
            if restart_game == "y":
                continue
            elif restart_game == "n":
                print("Thank you for playing!")
                return False



def display_game(): # הצגה ראשונית
    print("\n" + "=" * 50)
    print("WELCOME TO".center(45))
    print("Guess the word game".center(45))
    print("=" * 50)


def random_word(): # # בחירת מילה רנדומלית מתוך רשימה ושמירת הערך שלה
    word_list = ["apple","tomato","water","junk","coil"]
    word = random.choice(word_list)
    return word


def progress(word_check,guessed_letters): # מקבל את המילה הרנדומלית והרשימה הריקה
    print("Word: ",end="")
    for letter in word_check:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    return False


def validate_guess(word,guessed_letters):# פונקציה שעוברת על כל אות במילה הרנדומלית אם נוחשו כל האותיות ונכנסו למערך החדש
    for letter in word: # במידה ואחרי האימות יצא שבמילה שלנו וכל האותיות שנחשנו מדוייק יחזור TRUE אחרת FALSE
        if letter not in guessed_letters:
            return False
    return True