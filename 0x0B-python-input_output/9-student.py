#!/usr/bin/python3
"""This module contains Student
that defines a student by:
"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Arguments:
            firs_name - first name of the student
            last_name - last name of the student
            age - age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of a Student instance
        """
        return self.
