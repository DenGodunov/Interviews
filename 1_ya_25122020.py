def num_of_sets(l):
    """
    num_of_sets(list of strings) -> int
    num_of_sets(['a']) -> 1
    """
    distinct_sweets = set(l) #let's find all distinct sweets from input list
    dict_of = {} #empty dict to store key:value (sweet:number of occurrences)

    for i in distinct_sweets:
        dict_of[i] = l.count(i)
        
    key_min = min(dict_of.keys(), key=(lambda k: dict_of[k]))
    return dict_of[key_min]
    
assert num_of_sets(['a', 'b', 'c']) == 1
assert num_of_sets(['a', 'b', 'c', 'a', 'b', 'c','d']) == 1
assert num_of_sets(['a', 'b', 'c', 'a', 'b', 'c']) == 2
