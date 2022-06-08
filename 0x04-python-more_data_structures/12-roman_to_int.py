#!/usr/bin/python3
def roman_to_int(roman_string):
    aux = 0
    roman_dict =\
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) != str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        for j in roman_dict:
            if i > 0:
                if roman_string[i] == j \
                        and roman_dict[roman_string[i - 1]] >= roman_dict[j]:
                    aux += roman_dict[j]
                elif roman_string[i] == j \
                        and roman_dict[roman_string[i - 1]] < roman_dict[j]:
                    aux -= roman_dict[roman_string[i - 1]]
                    aux -= roman_dict[roman_string[i - 1]]
                    aux += roman_dict[j]
            elif roman_string[i] == j:
                aux += roman_dict[j]
    return 
