#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    max_tuple = max(len(tuple_a), len(tuple_b))

    if max_tuple == 0:
        return (0, 0)

    if len(tuple_a) == 0:
        if len(tuple_b) == 1:
            return (tuple_b[0], 0)
        return tuple_b

    if len(tuple_b) == 0:
        if len(tuple_a) == 1:
            return (tuple_a[0], 0)
        return tuple_a

    a = b = 0
    if len(tuple_a) == 1 and len(tuple_b) == 1:
        a = tuple_a[0] + tuple_b[0]
    elif len(tuple_a) == 1:
        a = tuple_a[0] + tuple_b[0]
        b = 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + 0
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]

    return (a, b)
