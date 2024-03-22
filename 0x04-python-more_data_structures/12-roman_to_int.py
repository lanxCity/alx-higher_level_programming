#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_to_int = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50,
            'C': 100, 'D': 500,
            'M': 1000
            }

    if not roman_string:
        return (0)

    for i in roman_string:
        if i not in roman_to_int:
            return (0)

    user_input = roman_string
    input_len = len(user_input)
    total = 0
    next_is_removed = False

    for i in range(len(user_input)):
        if next_is_removed:
            next_is_removed = False
            continue

        curr = user_input[i]
        next_roman = 0

        if ((i + 1) < input_len):
            next_roman = user_input[i + 1]

        if next_roman not in roman_to_int or (
                roman_to_int[curr] >= roman_to_int[next_roman]):
            total += roman_to_int[curr]
        else:
            total += (roman_to_int[next_roman] - roman_to_int[curr])
            next_is_removed = True

    return (total)
