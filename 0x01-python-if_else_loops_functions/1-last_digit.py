#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number2 = number * (-1)
    number1 = (number2 % 10 * (-1))
else:
    number1 = number % 10
print("Last digit of {} is {} and is ".format(number, number1), end="")
if number > 5:
    print("greater than 5")
elif number1 == 0:
    print("0")
else:
    print("less than 6 and not 0")
