# Author: Azad
# Date: 4/5/18
# Desc: Write a program that takes a list of numbers
#       (for example, a = [5, 10, 15, 20, 25])
#       and makes a new list of only the first and last elements of the given list.
#       For practice, write this code inside a function.
#________________________________________________________________________________________

a = [5, 10, 15, 20, 25]

def get_start_and_end(list):
    return [list[0], list[len(list)-1]]

print(get_start_and_end(a))
