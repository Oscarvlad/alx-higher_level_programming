#!/usr/bin/python3
"""This module contain a class that
prevents the user from dynamically creating
new instance attributes, except if the
new instance attribute is called first_name.
"""


class LockedClass:
    """This class creates instance
    only if is called first_name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        """This method initialize the object."""
        if hasattr(self, first_name):
            self.first_name = first_name
