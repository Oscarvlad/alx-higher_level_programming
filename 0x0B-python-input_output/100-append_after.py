#!/usr/bin/python3
"""This module contanins a function
 that inserts a line of text to a file,
 after each line containing a specific string
 """


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string"""
    idx = 0

    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        idx += 1
        if search_string in line:
            lines.insert(idx, new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        lines = "".join(lines)
        f.write(lines)
