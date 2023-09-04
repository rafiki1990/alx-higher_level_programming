#!/usr/bin/python3
"""3-say_my_name module."""


def say_my_name(first_name, last_name=""):
    """
    Represent Function say_my_name that returns the first and last names.

    Args:
    first_name(str): the first name to be returned.
    last_name(str): The last name to be returned.
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
    elif not first_name:
        raise TypeError('At least one argument is required')
    else:
        raise TypeError(
            'first_name must be a string'
            if not isinstance(first_name, str)
            else 'last_name must be a string')
