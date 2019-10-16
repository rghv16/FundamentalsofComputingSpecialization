"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    new_list = [0]*len(line)
    ind = 0
    for ele in line:
        if new_line[ind] == 0:
            new_line[ind] = ele
        elif new_line[ind] == ele:
            new_line[ind] += ele
        else:
            ind += 1
            new_line[ind] = ele
    return new_list
