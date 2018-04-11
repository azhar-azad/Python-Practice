# Author: Azad
# Date: 4/5/18
# Desc: Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
#       Make sure to ask the user to enter the number of numbers in the sequence to generate.
#       (Hint: The Fibonacci sequence is a sequence of numbers where
#       the next number in the sequence is the sum of the previous two numbers in the sequence.
#       The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#_____________________________________________________________________________________________________________

# To get user input
def get_input(prompt):
    return int(input(prompt))

# Returns the nth fibonacci number
def fibonacci_of(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_of(n-1) + fibonacci_of(n-2)

# Generates a list of fibonacci numbers sequence up to n
def fibonacci_seq_upto(n):
    fib_list = []
    for i in range(1, n+1):
        fib_list.append(fibonacci_of(i))
    return fib_list


n = get_input("How many fibonacci numbers would you like to generate: ")

print("Fibonacci sequence up to " + str(n) + " is \n" + str(fibonacci_seq_upto(n)))