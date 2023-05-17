#!/usr/bin/python3
# 1-search_replace.py
# Batsirai Malvern Mugomba


def search_replace(my_list, search, replace):
    "copy list"
    new_list = my_list.copy()
    "iterate list"
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
