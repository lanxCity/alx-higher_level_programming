#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10

    if number < 0 and last_digit != 0:
        last_digit = (last_digit - 10) * -1

    print("{}".format(last_digit), end='')
    return last_digit
