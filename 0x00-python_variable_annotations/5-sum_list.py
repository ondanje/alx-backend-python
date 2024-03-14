#!/usr/bin/env python3
"""
type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    looping over the list using a for loop and the adding the sum
    of the items of the list
    """
    sum: float = 0
    for x in range(len(input_list)):
        """print(input_list[x])"""

        sum += input_list[x]

    return sum
