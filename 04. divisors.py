# Author: Azad
# Date: 4/1/18
# Desc: Create a program that asks the user for a number
#       and then prints out a list of all the divisors of that number.
#       (If you don’t know what a divisor is, it is a number that divides evenly into another number.
#       For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# ------------------------------------------------------------------------------------------------------

num = int(input("Enter an integer number: "))
divisors = []

for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)
print("The list of all the divisors of that number is ")
print(divisors)

