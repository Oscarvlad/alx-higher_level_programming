#!/usr/bin/python3
def uniq_add(my_list=[]):
    auxiliar_list = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in auxiliar_list:
            auxiliar_list.append(my_list[i])
    for i in auxiliar_list:
        result = result + i
    return 
