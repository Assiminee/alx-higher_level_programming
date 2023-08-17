#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        top, bot = 0, 0
        for tp in my_list:
            top += tp[0] * tp[1]
            bot += tp[1]
        return top/bot
    return 0
