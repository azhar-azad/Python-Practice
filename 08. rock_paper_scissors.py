# Author: Azad
# Date: 4/2/18
# Desc: Make a two-player Rock-Paper-Scissors game.
#       (Hint: Ask for player plays (using input), compare them,
#       print out a message of congratulations to the winner,
#       and ask if the players want to start a new game)
#
#       Remember the rules:
#           Rock beats scissors
#           Scissors beats paper
#           Paper beats rock
# --------------------------------------------------------------------



def comp_turn():
    import random
    choice = random.choice(['r', 'p', 's'])
    if choice == 'r':
        print("Computer chooses Rock.")
    elif choice == 'p':
        print("Computer chooses Paper.")
    elif choice == 's':
        print("Computer chooses Scissors.")
    return choice

def user_turn():
    print("r for Rock, p for Paper, s for Scissors.")
    choice = input("Enter your choice: ")
    if choice == 'r':
        print("You choose Rock.")
    elif choice == 'p':
        print("You choose Paper.")
    elif choice == 's':
        print("You choose Scissors.")
    else:
        inv_choice()
    return choice

def comp_win():
    print("Computer wins.")
    return input("Play again? y/n: ")

def user_win():
    print("You win.")
    return input("Play again? y/n: ")

def draw():
    print("Draw game.")

def inv_choice():
    print("Invalid Choice.\nProgram is terminated")



print("Welcome to Rock, Paper, Scissors game.")

while True:
    u = user_turn()
    c = comp_turn()

    if u == 'r':
        if c == 'r':
            ch = draw()
            if ch == 'n':
                break
        elif c == 'p':
            ch = comp_win()
            if ch == 'n':
                break
        elif c == 's':
            ch = user_win()
            if ch == 'n':
                break
        else:
            inv_choice()
            break

    elif u == 'p':
        if c == 'p':
            ch = draw()
            if ch == 'n':
                break
        elif c == 's':
            ch = comp_win()
            if ch == 'n':
                break
        elif c == 'r':
            ch = user_win()
            if ch == 'n':
                break
        else:
            inv_choice()
            break

    elif u == 's':
        if c == 's':
            ch = draw()
            if ch == 'n':
                break
        elif c == 'r':
            ch = comp_win()
            if ch == 'n':
                break
        elif c == 'p':
            ch = user_win()
            if ch == 'n':
                break
        else:
            inv_choice()
            break

    else:
        inv_choice()
        break



