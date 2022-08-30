#!/usr/bin/python3
def new_in_list(li, idx, element):
    new = li[:]
    size = len(li)
    if (0 <= idx < size):
        new[idx] = element
    return (new)
