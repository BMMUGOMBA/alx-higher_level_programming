#!/usr/bin/python3
#Batsirai M Mugomba


def no_c(my_string):
    my_string = ''.join(char for char in my_string if char not in 'Cc')
    return my_string
