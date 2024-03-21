#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    dic_values = list(new_dic.values())

    dic_values_by_2 = list(map(
            (lambda x: x * 2), dic_values))

    count = 0
    for key in new_dic:
        new_dic.update(
                {key: dic_values_by_2[count]})
        count += 1
    return new_dic
