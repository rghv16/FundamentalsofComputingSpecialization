"""
Principal of computing part 1
week 1 : Merge function for 2048 game.
Author : raghav atreya
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.

    """
    new_list = [0] * len(line)
    ind = 0

    for ele in line:
        if ele == 0:
            continue
        elif new_list[ind] == 0:
            new_list[ind] = ele
        elif new_list[ind] == ele:
            new_list[ind] += ele
            ind += 1
        else:
            ind += 1
            new_list[ind] = ele

    return new_list


# print(merge([8, 0, 8]))
