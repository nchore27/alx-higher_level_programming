#!/usr/bin/python3
"""defines a function pascal_triangle"""


def pascal_triangle(n):
    """prints the pascal triangle represented
    by list of lists of integers
    Args:
        n: length of list
    """
    if n <= 0:
        return list()
    pas = [[1]]
    while len(pas) != n:
        triangle = pas[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        pas.append(temp)
    return pas
