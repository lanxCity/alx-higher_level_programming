#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_hidden_4 = dir(hidden_4)

    for func in list_hidden_4:
        if func[:2] != "__":
            print("{}".format(func))
