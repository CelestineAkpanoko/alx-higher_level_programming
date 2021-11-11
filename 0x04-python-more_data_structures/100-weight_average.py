#!/usr/bin/python3
def weight_average(my_list=[]):
    average, base_total, total = 0, 0, 0
    if my_list == []:
        return 0
    else:
        for i in my_list:
            total += (i[0]*i[1])
            base_total += i[1]
        average = total / base_total
        return average