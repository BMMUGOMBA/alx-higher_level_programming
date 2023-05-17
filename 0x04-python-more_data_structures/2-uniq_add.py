#!/usr/bin/python3
# 2-uniq_add.py
# Batsirai M Mugomba


def uniq_add(my_list=[]):
   
    total = 0
    "channge list to unique set"
    for x in set(my_list):
        "add to result"
        total += x
    return (total)
