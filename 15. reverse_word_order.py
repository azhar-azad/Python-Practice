# Author: Azad
# Date: 4/11/18
# Desc: Write a program (using functions!) that asks the user for a long string containing multiple words.
#       Print back to the user the same string, except with the words in backwards order.
#       For example, say I type the string:
#           My name is Michele
#       Then I would see the string:
#           Michele is name My
#       shown back to me.
#___________________________________________________________________________________________________________

# Returns user input with a prompt
def get_input(prompt):
    return input(prompt)

# Converts a given string to a list
def string_to_list(str):
    return str.split()

# Returns a given list in reverse order
def reverse_list(l):
    length = len(l)                         # calculates the length of l
    reverse_str = []                        # an empty list to store the output
    for i in range(length-1, -1, -1):       # loops through the last to first item in the list
        reverse_str.append(l[i])            # and appends them to the empty list
    return reverse_str

# Converts a given list to a string
def list_to_str(l):
    return ' '.join(l)


user_str = get_input("Enter a string: ")

print("You string in reverse order is: \n" + list_to_str(reverse_list(string_to_list(user_str))))