#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        ans = 0
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        except TypeError:
            print("{}".format("wrong type"))
        except IndexError:
            print("{}".format("out of range"))
        finally:
            new_list.append(ans)
    return new_list
