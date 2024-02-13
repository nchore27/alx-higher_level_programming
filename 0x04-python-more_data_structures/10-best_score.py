#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    result = list(a_dictionary.keys())[0]
    highest = a_dictionary[result]
    for i, j in a_dictionary.items():
        if j > highest:
            highest = j
            result = i
    return result
