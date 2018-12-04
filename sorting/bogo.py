"""
Sort a list by shuffling until we reach a sorted permutation.
Author: Pairode Jaroensri
Last visited: May 10, 2017
"""

import random

def shuffle(lst):
    result = []
    used_indice = []
    lst_length = len(lst)
    while len(used_indice) != lst_length:
        index = random.randint(0, lst_length - 1)
        if index not in used_indice:
            used_indice.append(index)
            result.append(lst[index])
    return result

def is_sorted(lst):
    i = lst[0]
    for k in lst:
        if i > k:
            return False
        i = k
    return True

def bogo_sort(lst):
    result = lst[:]
    while not is_sorted(result):
        print(result)
        result = shuffle(result)
    return result

def improved_bogo_sort(lst):
    seen = []
    result = lst[:]
    while not is_sorted(result) and result not in seen:
        print(result)
        seen.append(result)
        result = shuffle(result)
    return result
