
def height():
    
    data = [
        [2, 2, 2, 4, 2],
        [0, 2, 0, 4, 0],
    ]
    
    return len(data)

def width():

    data = [
        [2, 2, 2, 4, 2],
        [0, 2, 0, 4, 0],
    ]
    
    return len(data[0])

def merge(line):
    """
    Merge Function for the 2048 Game 
    """
    new_line = [0]*len(line)
    ind = 0
    for ele in line:
        if ele == 0:
            continue
        elif new_line[ind] == 0:
            new_line[ind] = ele
        elif new_line[ind] == ele:
            new_line[ind] += ele
            ind += 1
        else:
            ind += 1
            new_line[ind] = ele
    return new_line

def is_equal(list1, list2):
    """This function return True"""
    for i in range(len(list2)):
        if list2[i] != list1[i]:
            return False
    return True


def generate(direction):
    outer, inner = height(), width()
    swap_index = False
    if direction in ('up', 'down'):
        outer, inner = inner, outer
        swap_index = True

    start, end = 0, inner
    offset = 1
    if direction in ('left', 'up'):
        start, end = end-1, start -1
        offset = -1
    
    print('direction {} Outer {} Inner {} offset {} start {} end {}'.format(direction,\
     outer, inner, offset, start, end))

    is_change = False

    data = [
        [2, 2, 2, 4, 2],
        [0, 2, 0, 4, 0],
    ]
    print('\t')
    print(*data, sep = "\n")
    for i in range(outer):
        # print('------ Row {} -----'.format(i))
        row_data = []
        for j in range(start, end, offset):
            if swap_index:
                row_data.append(data[j][i])
            else:
                row_data.append(data[i][j])

        # print('calling move function')
        print('row_data \t ',row_data)
        new_line = merge(row_data)
        
        print('new_line \t', new_line)
        # if return true means no change in list
        # if not is_equal(row_data, new_line):
        #     is_change = True

        
        if direction in ('right', 'down'):
            new_line = new_line[::-1]

        for j in range(start, end, offset):
            if swap_index:
                data[j][i] = new_line[j]
            else:
                data[i][j] = new_line[j]
    print('Final Answer')
    print(*data, sep = "\n")

    if is_change:
        print('Call new tile function')





if __name__ == '__main__':
    generate('up')
    generate('down')
    generate('left')
    generate('right')
    
