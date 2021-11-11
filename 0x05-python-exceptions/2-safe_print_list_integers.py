#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and val != x:
                print('{:d}'.format(my_list[i]), end='')
                val += 1
        except TypeError:
            continue

    print()

    return val
