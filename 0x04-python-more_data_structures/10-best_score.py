#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        dic_values = list(a_dictionary.values())

        max_value_idx = dic_values.index(max(dic_values))
        dic_keys = list(a_dictionary.keys())

        best_key = dic_keys[max_value_idx]

        return best_key
    return
