import sys

def num_of_sets(l):
    distinct_sweets = set(l)
    dict_of = {}
    for i in distinct_sweets:
        dict_of[i] = l.count(i)
    key_min = min(dict_of.keys(), key=(lambda k: dict_of[k]))
    print(dict_of[key_min])
num_of_sets(['a', 'b', 'c'])
num_of_sets(['a', 'b', 'c', 'a', 'b', 'c','d'])
num_of_sets(['a', 'b', 'c', 'a', 'b', 'c'])
