#!/usr/bin/python3
#Batsirai M Mugomba


def replace_in_list(my_list, idx, element):
    # if list == []:
    #     return my_list
    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list

    else:
        my_list[idx] = element
        return my_list
