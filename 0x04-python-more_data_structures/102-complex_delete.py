#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for item in new_dic.items():
        if item[1] == value:
            del a_dictionary[item[0]]
    return a_dictionary
