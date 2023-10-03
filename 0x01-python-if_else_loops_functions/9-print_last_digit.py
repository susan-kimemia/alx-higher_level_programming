#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_dgt = number % -(10)
        print(-(last_dgt), end="")
    else:
        last_dgt = number % 10
        print(last_dgt, end="")
    return abs(last_dgt)
