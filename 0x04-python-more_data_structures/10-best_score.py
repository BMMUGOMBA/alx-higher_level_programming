#!/usr/bin/python3
# 10-best_score.py
# Batsirai M Mugomba


def best_score(a_dictionary):
    
    v = list(a_dictionary.values())
    k = list(a_dictionary.keys())
    return k[v.index(max(v))]
