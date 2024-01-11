#!/usr/bin/python3

def weight_average(my_list=[]):
    '''
    a function that returns the weighted average of all integers tuple

    Args:
        my_list : list
    Returns:
        float
    '''
    if not my_list:
        return 0
    else:
        numerator = sum([score * weight for score, weight in my_list])
        denominator = sum([weight for score, weight in my_list])
        return numerator / denominator
