#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dgt = number % -10
else:
    last_dgt = number % 10
if last_dgt > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, last_dgt))
elif last_dgt < 6 and last_dgt != 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, last_dgt))
else:
    print("Last digit of {} is 0 and is 0".format(number))
