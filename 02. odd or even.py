# Author: Azad
# Date: 4/1/18
# Desc: Ask the user for a number. Depending on whether the number is even or odd,
#       print out an appropriate message to the user.
#       Hint: how does an even / odd number react differently when divided by 2?
#   Extras:
#       1. If the number is a multiple of 4, print out a different message.
#       2. Ask the user for two numbers:
#       one number to check (call it num) and one number to divide by (check).
#       If check divides evenly into num, tell that to the user.
#       If not, print a different appropriate message.
# -----------------------------------------------------------------------------------------

num = int(input("Enter an integer number: "))

if num % 2 == 0:
    print(str(num) + " is even", end='')
    # Extras 1:
    if num % 4 == 0:
        print(" and divisible by 4.")
    else:
        print(" but not divisible by 4.")
else:
    print(str(num) + " is odd and therefore not divisible by 4.")


# Extras 2:
check = int(input("Enter another integer number to divide: "))

if num % check == 0:
    print(str(num) + " is evenly divisible by " + str(check))
else:
    print(str(num) + " is not evenly divisible by " + str(check))
