#!/usr/bin/python3
"""This module gives solution to the N queens puzzle"""
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not (sys.argv[1]).isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    size = int(sys.argv[1])

    i = 1
    while i < size - 1:
        result = []
        init = [0, i]
        result.append(init)
        test_position(size, result)
        i += 1


def accept(i, j, result, size):
    """accept position if is valid
    Returns: True if accepted otherwise False.
    """
    decision = True
    for l in result:
        # Test vertical and horizontal
        if i == l[0] or j == l[1]:
            decision = False
        elif diagonals_check(i, j, l, size) is True:
            decision = False
    return decision


def diagonals_check(i, j, l, size):
    """diagonals_check determine if position i,j is diagonal to reference value l
    Args:
        i ([type]): [description]
        j ([type]): [description]
        l ([type]): [description]
    """
    i_change = 0
    j_change = 0
    # Test diagonals positive values i and j
    i_change = l[0]
    j_change = l[1]
    i_change += 1
    j_change += 1
    while i_change < size and j_change < size:
        if i == i_change and j == j_change:
            return True
        i_change += 1
        j_change += 1
    # Test diagonals i positive values j negative values
    i_change = l[0]
    j_change = l[1]
    i_change += 1
    j_change -= 1
    while i_change < size and j_change >= 0:
        if i == i_change and j == j_change:
            return True
        i_change += 1
        j_change -= 1
    # Test diagonals j positive values i negative values
    i_change = l[0]
    j_change = l[1]
    i_change -= 1
    j_change += 1
    while i_change >= 0 and j_change < size:
        if i == i_change and j == j_change:
            return True
        i_change -= 1
        j_change += 1
    # Test diagonals both i and j negative values
    i_change = l[0]
    j_change = l[1]
    i_change -= 1
    j_change -= 1
    while i_change >= 0 and j_change >= 0:
        if i == i_change and j == j_change:
            return True
        i_change -= 1
        j_change -= 1
    return False


def test_position(size, result):
    """test_position [summary]
    [extended_summary]
    """
    i = 0
    # Test different positions
    while i < size:
        j = 0
        while j < size:
            if accept(i, j, result, size) is True:
                new = [i, j]
                result.append(new)
                break
            j += 1
        i += 1
    print(result)

main()
