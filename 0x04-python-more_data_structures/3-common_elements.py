#!/usr/bin/python3
# 3-common_elements.py
# Batsirai M Mugomba


def common_elements(set_1, set_2):
    set_3 = set(set_1 - (set(set_1) - set(set_2)))
    return (set_3)
