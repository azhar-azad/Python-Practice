# Author: Azad
# Date: 4/6/18
# Desc: Write a program (function!) that takes a list and returns a new list
#       that contains all the elements of the first list minus all the duplicates.
#   Extras:
#       1. Write two different functions to do this -
#       one using a loop and constructing a list, and another using sets.
#___________________________________________________________________________________________________________

# Function using set
def rmv_list_duplicates_v1(lst):
    return list(set(lst))


# Function using loop
def rmv_list_duplicates_v2(lst):
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list



print(rmv_list_duplicates_v1([1, 2, 3, 4, 2, 2]))
print(rmv_list_duplicates_v2([1, 2, 3, 4, 2, 2]))