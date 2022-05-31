#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        character = chr(ord(str[i]) - 32)
        print(f"{character}" if str[i].islower() else f"{str[i]}", end="")
    print("\n", end="")
