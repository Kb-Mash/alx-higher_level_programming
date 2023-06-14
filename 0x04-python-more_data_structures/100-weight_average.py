#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if my_list and len(my_list):
        sumOf = 0
        sizeOf = 0
        for i in my_list:
            sumOf += (i[0] * i[1])
            sizeOf += (i[1])
        return (sumOf / sizeOf)
    return (0)
