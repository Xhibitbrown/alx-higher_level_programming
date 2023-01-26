#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    "prints the first x elements of a list and only integers"
    i = pichu = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            pich += 1
        except(TypeError, ValueError):
            continue
        return pichu
