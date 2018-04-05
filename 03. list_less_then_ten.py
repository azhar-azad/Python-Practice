# Author: Azad
# Date: 4/1/18
# Desc: Take a list, say for example this one:
#       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#       and write a program that prints out all the elements of the list that are less than 5.
#
#   Extras:
#       1. Instead of printing the elements one by one,
#       make a new list that has all the elements less than 5 from this list in it and print out this new list.
#       2. Write this in one line of Python.
#       3. Ask the user for a number
#       and return a list that contains only elements from the original list
#       that are smaller than that number given by the user.
#-------------------------------------------------------------------------------------------------------------

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list:
    if i < 5:
        print(i)
print("\n")

# Extras 1:
print("Extras 1: ")
new_list = []
for i in list:
    if i < 5:
        new_list.append(i)
print(new_list)
print("\n")

# Extras 2:
print("Extras 2: ")
print("Couldn't do that.")
print("\n")

# Extras 3:
print("Extras 3: ")
num = int(input("Enter an integer number: "))
new_list = []
for i in list:
    if i < num:
        new_list.append(i)
print(new_list)