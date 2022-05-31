#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i < x:
            print(f"{i}{x}, " if i != 8 else f"{i}{x}\n", end="")
