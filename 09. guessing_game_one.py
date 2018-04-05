# Author: Azad
# Date: 4/2/18
# Desc: Generate a random number between 1 and 100 (including 1 and 100).
#       Ask the user to guess the number,
#       then tell them whether they guessed too low, too high, or exactly right.
#
#   Extras:
#       1. Keep the game going until the user types “exit”
#       2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
# ___________________________________________________________________________________________________

def get_number():
    import random
    return random.randint(1, 101)

def get_user_guess():
    return input("Guess the number: ")

def gameplay():
    num = get_number()
    print(num)
    count = 0

    while True:
        if get_user_guess().lower() == 'exit':
            break

        while True:

            count += 1

            if num > int(get_user_guess()):
                print("Low, Guess higher.   Count = " + str(count))

            elif  num < int(get_user_guess()):
                print("High, Guess lower.   Count = " + str(count))

            elif num == int(get_user_guess()):
                print("You won.")
                if count < 2:
                    print("You needed " + str(count) + " tries. Impressive.")
                elif count < 10:
                    print("You needed " + str(count) + " tries. Pretty good.")
                else:
                    print("You needed " + str(count) + " tries. Not that efficient.")
                break





print("Guess the magic number in the range (1, 100)")
print("Type exit to exit.")
gameplay()
