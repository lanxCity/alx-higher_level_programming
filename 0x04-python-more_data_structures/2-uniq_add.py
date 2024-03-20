#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []

    for num in my_list:
        new_list.append(num) if num not in new_list else None

    rslt = 0

    for x in new_list:
        rslt += x

    return rslt
