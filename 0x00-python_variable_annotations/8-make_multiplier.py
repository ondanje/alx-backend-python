#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that returns a function that multipliers a float by multiplier
    """
    def multipy(x: float) -> float:
        """the function that is used returned by the above function"""
        return float(x * multiplier)
    return multipy
