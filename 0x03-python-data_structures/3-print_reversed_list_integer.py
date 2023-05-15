#!/usr/bin/python3
#Batsirai M Mugomba


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print('', end='')
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
