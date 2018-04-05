# Author: Azad
# Date: 4/1/18
# Desc: Ask the user for a string and print out whether this string is a palindrome or not.
#       (A palindrome is a string that reads the same forwards and backwards.)
# -------------------------------------------------------------------------------------------

def if_palindrome(str):
    length = len(str)
    l = length

    while l > 0:
        if str[length - l] != str[l-1]:
            return False
        l -= 1

    return True

string = input("Enter a string: ")
if if_palindrome(string):
    print(string + " is a palindrome.")
else:
    print(string + " is not a palindrome.")
