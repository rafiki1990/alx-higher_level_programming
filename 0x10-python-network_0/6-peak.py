#!/usr/bin/python3
"""
Module: 6-peak.

This module provides a function to find a peak in a list of
unsorted integers using a divide-and-conquer approach.
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers using a divide-and-conquer.

    Args:
    list_of_integers (list): The list of unsorted integers.

    Returns:
    int or None: The peak integer if found, or None if the list is empty.

    Complexity:
    O(nlog(n))
    """
    # Check if the list is empty
    if len(list_of_integers) == 0:
        return None

    # Base case: If the list has only one element, it's a peak
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    # Find the middle index of the list
    mid = len(list_of_integers) // 2

    # Compare the middle element with its neighbors
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        # If the middle element is smaller than the left neighbor,
        # recursively search the left half of the list
        return find_peak(list_of_integers[:mid])
    elif list_of_integers[mid] < list_of_integers[mid + 1]:
        # If the middle element is smaller than the right neighbor,
        # recursively search the right half of the list
        return find_peak(list_of_integers[mid + 1:])
    else:
        # If neither condition is met, the middle element is a peak
        return list_of_integers[mid]
