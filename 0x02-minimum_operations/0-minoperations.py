#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    now = 1
    starts = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            starts = now
            now += starts
            counter += 2
        else:
            now += starts
            counter += 1
    return counter
