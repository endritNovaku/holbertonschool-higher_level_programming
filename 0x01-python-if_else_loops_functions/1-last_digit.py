#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    number1 = number % 10
else number < 0:
    number1 = (number - number - number) % 10
    number1 = number1 - number1 - number1
if number1 > 5:
    print("Last digit of {} is {} {}".format(number, number1, "and is greater then 5"))
elif number1 == 0:
    print("Last digit of {} is {} {}".format(number, number1, "and is 0"))
elif number1 < 6 and not 0:
    print("Last digit of {} is {} {}".format(number, number1, "and is less then 6 and not 0"))
