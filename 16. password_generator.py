# Author: Azad
# Date: 4/12/18
# Desc: Write a password generator in Python. Be creative with how you generate passwords
#        - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#       The passwords should be random, generating a new password every time the user asks for a new password.
#       Include your run-time code in a main method.
#   Extra:
#       Ask the user how strong they want their password to be.
#       For weak passwords, pick a word or two from a list.
#_____________________________________________________________________________________________________________

import random

# Gets user input
def get_input(prompt):
    return input(prompt)

# Generates a random uppercase letter
def upcase_letter_gen():
    return chr(random.randint(65, 90))

# Generates a random lowercase letter
def lowcase_letter_gen():
    return chr(random.randint(97, 122))

# Generates a random integer number
def number_gen():
    return chr(random.randint(48, 57))

# Generates a random printable symbol
def symbol_gen():
    symbol_list = []                                    # empty list to hold symbols
    symbol_list.append(chr(random.randint(33, 47)))
    symbol_list.append(chr(random.randint(58, 64)))
    symbol_list.append(chr(random.randint(91, 96)))
    symbol_list.append(chr(random.randint(123, 126)))

    return symbol_list[random.randint(0, 3)]            # returns a random symbol from the symbol list

# Generates a random password of given length
def passwd_gen(type, length):
    passwd = []                                     # empty list to hold the password

    if type == 'w':                                 # for weak password
        for i in range(0, length):                  # generates only lowercase letters
            passwd.append(lowcase_letter_gen())

    elif type == 'm':
        char_list = []
        for i in range(0, length):
            char_list.append(upcase_letter_gen())   # uppercase, lowercase letters and numbers
            char_list.append(lowcase_letter_gen())  # are added to a temporary character list
            char_list.append(number_gen())          # such as char_list = [A, a, 0]
            passwd.append(char_list[random.randint(0, 2)])  # a random char from char_list is selected

    elif type == 's':
        for i in range(0, length):
            char_list = []
            char_list.append(upcase_letter_gen())       # uppercase, lowercase letters, numbers
            char_list.append(lowcase_letter_gen())      # and symbols are added to a
            char_list.append(number_gen())              # temporary character list
            char_list.append(symbol_gen())              # such as char_list = [A, a, 0, @]
            passwd.append(char_list[random.randint(0, 3)])  # a random char from char_list is selected

    return ''.join(passwd)      # passwd list is converted to string and returned

# Getting user input
print("Enter password type and length: ")
print("     1. Weak password(press w)")
print("     2. Medium-strong password(press m)")
print("     3. Strong password(press s)")
type = get_input("Enter choice: ")
length = int(get_input("Enter password length: "))

print("Generated password as your requirement is " + passwd_gen(type, length))



