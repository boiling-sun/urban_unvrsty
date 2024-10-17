"""
Given an array with exactly 5 strings "a", "b" or "c" , 
check if the array contains three and two of the same values.
"""

from collections import Counter

def check_three_and_two(array):
    counter = Counter(array)
    return 3 in counter.values() and 2 in counter.values()

