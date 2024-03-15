#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    (
            print("{} argument".format(len(argv) - 1), end="")
            if len(argv) == 2
            else print("{} arguments".format(len(argv) - 1), end="")

            )

    print("{}".format(":")) if (len(argv) - 1) else print("{}".format("."))

    if len(argv) - 1:

        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
