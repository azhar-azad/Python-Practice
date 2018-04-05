# Author: Azad
# Date: 4/1/18
# Desc: Create a program that asks the user to enter their name and their age.
#       Print out a message addressed to them that tells them the year that they will turn 100 years old.
#       Extras:
#           1. Add on to the previous program by asking the user for another number
#           and printing out that many copies of the previous message.
#           (Hint: order of operations exists in Python)
#           2. Print out that many copies of the previous message on separate lines.
#           (Hint: the string "\n is the same as pressing the ENTER button)
# -----------------------------------------------------------------------------------------------------------

name = input("Enter your name: ")
age = input("Enter your age: ")
repeat = input("Enter the number of times the message to be repeated: ")
r = int(repeat)
curnt_year = 2018

# printing on single line
while r != 0:
    print("You are " + name + " and you will turn 100 years old in " + str(curnt_year - int(age) + 100), end='')
    r -= 1

# printing on seperate lines
r = int(repeat)
while r != 0:
    print("You are " + name + " and you will turn 100 years old in " + str(curnt_year - int(age) + 100))
    r -= 1

