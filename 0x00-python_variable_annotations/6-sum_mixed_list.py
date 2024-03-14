#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import Union


def sum_mixed_list(mxd_list: Union[int | float]) -> float:
    """
    using the | operator to indicate that the type
    could be either int or float
    """
    sum = 0

    for x in range(len(mxd_list)):
        """print(mxd_list[x])"""

        sum += mxd_list[x]

    return sum
