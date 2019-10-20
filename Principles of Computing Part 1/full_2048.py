'''
2048 Full 
Author Raghav Atreya
raghavatreya16@gmail.com
http://www.codeskulptor.org/#user46_D9ZFAj6zr5jf3jy_1.py
'''


import poc_2048_gui
import random


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

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
    for ind in range(len(list2)):
        if list2[ind] != list1[ind]:
            return False
    return True

    
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid = [ [0 for _ in range(grid_width)] for _ in range(grid_height) ]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        grid1 = [
                [0 for _ in range(self.get_grid_width())]
                   for _ in range(self.get_grid_height())
                ]
        self._grid = grid1
        self.set_tile(0, 0, 2)
        self.set_tile(1, 1, 4)
        
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = '[['
        
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                string += str(self._grid[row][col]) + ', '
            string += ']\n'
        return string[:-1]+']'

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return len(self._grid)

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return len(self._grid[0])

    def move(self, direction):
        """ Move all tiles in the given direction and add a new tile 
        if any tiles moved.
        This can be resolved by splitting up the code into separate functions that can be called after.
        too many branches

        """
        
        outer, inner = self.get_grid_height(), self.get_grid_width()
        swap_index = False
        
        if direction in (UP, DOWN):
            outer, inner = inner, outer
            swap_index = True

        start, end = 0, inner
        offset = 1
        
        if direction in (DOWN, RIGHT):
            start = end - 1
            end = -1
            offset = -1
        
        is_change = False
        for ind in range(outer):
            row_data = []
            for jnd in range(start, end, offset):
                if swap_index:
                    print('Picking index jnd ',jnd,' ind ', ind,)
                    row_data.append(self._grid[jnd][ind])
                else:
                    print('Picking index ind ', ind, ' jnd ',jnd)
                    row_data.append(self._grid[ind][jnd])
            
            #if direction in (DOWN, ):
            print row_data    
            new_line = merge(row_data)
            if not is_equal(row_data, new_line):
                is_change = True
            print new_line
               
            if direction in (RIGHT, DOWN):
                temp = []
                while len(new_line) > 0:
                    temp.append(new_line.pop())
                    print "tempp ", temp
                new_line = temp
                print "row data changed ", new_line   
            for jnd in range(start, end, offset):
                if swap_index:
                    self._grid[jnd][ind] = new_line[jnd]
                else:
                    self._grid[ind][jnd] = new_line[jnd]
        
        if is_change:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        # two task randomly pick a square and insert a random value in it
        flag = True
        while flag:
            row = random.randint(0, self.get_grid_height()-1 )
            col = random.randint(0, self.get_grid_width()-1 )
            if self._grid[row][col] == 0:
                self.set_tile(row, col, random.choice([2, 2, 2, 2, 2, 4, 2, 2, 2, 2]))
                flag = False 

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]



===============================================
"""
    Clone of 2048 game.
"""

#import poc_2048_gui
import random


# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

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
    for ind in range(len(list2)):
        if list2[ind] != list1[ind]:
            return False
    return True

    
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid = [ [0 for _ in range(grid_width)] for _ in range(grid_height) ]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        grid1 = [
                [0 for _ in range(self.get_grid_width())]
                   for _ in range(self.get_grid_height())
                ]
        self._grid = grid1
        self.set_tile(0, 0, 2)
        self.set_tile(1, 1, 4)
        
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = '[['
        
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                string += str(self._grid[row][col]) + ', '
            string += ']\n'
        return string[:-1]+']'

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return len(self._grid)

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return len(self._grid[0])
        
    def move(self, direction):
        """ Move all tiles in the given direction and add a new tile 
        if any tiles moved.
        """
        
        outer, inner = self.get_grid_height(), self.get_grid_width()
        swap_index = False
        
        if direction in (UP, DOWN):
            outer, inner = inner, outer
            swap_index = True

        start, end = 0, inner
        offset = 1
        
        if direction in (DOWN, RIGHT):
            start = end - 1
            end = -1
            offset = -1
        
        is_change = False
        for ind in range(outer):
            row_data = []
            for jnd in range(start, end, offset):
                if swap_index:
                    print('Picking index jnd ',jnd,' ind ', ind,)
                    row_data.append(self._grid[jnd][ind])
                else:
                    print('Picking index ind ', ind, ' jnd ',jnd)
                    row_data.append(self._grid[ind][jnd])
            
            #if direction in (DOWN, ):
            print row_data    
            new_line = merge(row_data)
            if not is_equal(row_data, new_line):
                is_change = True
            print new_line
               
            if direction in (RIGHT, DOWN):
                temp = []
                while len(new_line) > 0:
                    temp.append(new_line.pop())
                    print "tempp ", temp
                new_line = temp
                print "row data changed ", new_line   
            for jnd in range(start, end, offset):
                if swap_index:
                    self._grid[jnd][ind] = new_line[jnd]
                else:
                    self._grid[ind][jnd] = new_line[jnd]
        
        if is_change:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        # two task randomly pick a square and insert a random value in it
        flag = True
        while flag:
            row = random.randint(0, self.get_grid_height()-1 )
            col = random.randint(0, self.get_grid_width()-1 )
            if self._grid[row][col] == 0:
                self.set_tile(row, col, random.choice([2, 2, 2, 2, 2, 4, 2, 2, 2, 2]))
                flag = False 

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]



obj = TwentyFortyEight(4, 4)
obj.set_tile(0, 0, 0)
obj.set_tile(0, 1, 0)
obj.set_tile(0, 2, 0)
obj.set_tile(0, 3, 0)
obj.set_tile(1, 0, 0)
obj.set_tile(1, 1, 8)
obj.set_tile(1, 2, 16)
obj.set_tile(1, 3, 0)
obj.set_tile(2, 0, 0)
obj.set_tile(2, 1, 16)
obj.set_tile(2, 2, 8)
obj.set_tile(2, 3, 0)
obj.set_tile(3, 0, 0)
obj.set_tile(3, 1, 0)
obj.set_tile(3, 2, 0)
obj.set_tile(3, 3, 0)
obj.move(DOWN)