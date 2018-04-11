# Author: Azad
# Date: 4/5/18
# Desc: Ask the user for a number and determine whether the number is prime or not.
#       (A prime number is a number that has no divisors except 1 and the number itself.).
#       Use functions.
#_______________________________________________________________________________________________

def get_input(prompt):
    return int(input(prompt))

def is_prime(n):
    if n < 2:
        return False

    import math

    flag = True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            flag = False
            break
    return flag


number = get_input("Enter an integer number: ")

if is_prime(number):
    print(str(number) + " is a prime number.")
else:
    print(str(number) + " is not a prime number.")