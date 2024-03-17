#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    max_tuple = max(len(tuple_a), len(tuple_b))

    if len(tuple_a) == 0:
        return tuple_b
    if len(tuple_b) == 0:
        return tuple_a

    if max_tuple >= 2:
        a = b = 0
        if len(tuple_a) == 1:
            a = tuple_a[0] + tuple_b[0]
            b = 0 + tuple_b[1]
        elif len(tuple_b) == 1:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + 0
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]

        return (a, b)
