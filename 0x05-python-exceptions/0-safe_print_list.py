#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    p = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            p += 1
        except:
            pass
    print()
    return p
