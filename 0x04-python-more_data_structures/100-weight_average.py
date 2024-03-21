#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total_weight = 0
        cumulative_weight_point = 0

        for item in my_list:
            score = item[0]
            weight = item[1]

            cumulative_weight_point += score * weight
            total_weight += weight

        cumulative_weight_point_avg = (
                cumulative_weight_point / total_weight)

        return cumulative_weight_point_avg

    return (0)
