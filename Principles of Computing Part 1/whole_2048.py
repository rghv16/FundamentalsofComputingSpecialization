"""
Clone of 2048 game.
"""

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
        string = ''
        
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                string += str(self._grid[row][col]) + ' '
            string += '\n'
            
        return string

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
        """
        Move all tiles in t
        he given direction and add
        a new tile if any tiles moved.
        """
        pass

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


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

