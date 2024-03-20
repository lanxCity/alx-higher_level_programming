#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = a_dictionary.copy()

    dic_keys = sorted(new_dic.keys())

    for key in dic_keys:
        print("{}: {}".format(key, new_dic.get(key)))
    return
