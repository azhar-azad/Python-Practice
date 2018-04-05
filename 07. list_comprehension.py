# Author: Azad
# Date: 4/2/18
# Desc: Let’s say I give you a list saved in a variable:
#       a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#       Write one line of Python that takes this list a and makes a new list
#       that has only the even elements of this list in it.
# -----------------------------------------------------------------------------------

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = [i for i in a if i % 2 == 0]
print(even_list)
print("\n")

print("Using a random list: ")

import random

rand_list = []
list_length = random.randint(5, 15)

while len(rand_list) < list_length:
    rand_list.append(random.randint(1, 75))

even_list = [i for i in rand_list if i % 2 == 0]

print(rand_list)
print(even_list)
