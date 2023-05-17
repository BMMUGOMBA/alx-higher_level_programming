#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Batsirai M Mugomba


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

