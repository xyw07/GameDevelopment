from tile import Tile
from game_manager import GameManager
MIN_BOARD_SIZE = 2


class Board:
    """An othello board"""
    def __init__(self, BOARD_SIZE):
        """
        :Int BOARD_SIZE: The size of the board,
        eg. BOARD_SIZE = 4 means a 4*4 board
        Board constructor
        """
        self.GRID_SIZE = 100
        self.STROKEWEIGHT = 4
        self.DEFAULT = 0
        self.BOARD_SIZE = BOARD_SIZE
        self.tiles = [[self.DEFAULT] * self.BOARD_SIZE
                      for i in range(self.BOARD_SIZE)]
        self.current_color = "black"

    @property
    def white_num(self):
        """
        the number of white tiles in the board
        """
        white_num = 0
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if (self.tiles[i][j] != self.DEFAULT):
                    if (self.tiles[i][j].color == "white"):
                        white_num += 1
        return white_num

    @property
    def black_num(self):
        """
        the number of black tiles in the board
        """
        black_num = 0
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if (self.tiles[i][j] != self.DEFAULT):
                    if (self.tiles[i][j].color == "black"):
                        black_num += 1
        return black_num

    def set_initial_tiles(self):
        """
        Create 4 initial tiles
        """
        if (self.BOARD_SIZE >= MIN_BOARD_SIZE):
            self.create_tile(self.BOARD_SIZE//2, self.BOARD_SIZE//2 - 1)
            self.create_tile(self.BOARD_SIZE//2 - 1, self.BOARD_SIZE//2 - 1)
            self.create_tile(self.BOARD_SIZE//2 - 1, self.BOARD_SIZE//2)
            self.create_tile(self.BOARD_SIZE//2, self.BOARD_SIZE//2)

    def change_turn(self):
        """
        change current turn
        """
        if self.current_color == "black":
            self.current_color = "white"
        else:
            self.current_color = "black"

    def create_tile(self, column, row):
        """
        :Int column: the column of the tile to be created
        :Int row: the row of the tile to be created
        Create a tile in the empty position
        with current turn's color
        and then change turn
        """
        if self.check_legal(column, row):
            t = Tile(column, row, self.current_color)
            self.tiles[row][column] = t
            self.change_turn()

    def check_legal(self, column, row):
        """
        :Int column: The column of the position to be checked
        :Int row: The row of the position to be checked
        only check if the current position alrealy been taken
        """
        return (self.tiles[row][column] == self.DEFAULT)

    def check_filled(self):
        """
        if the 2D list is filled, return True
        else, return Fasle
        """
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if (self.check_legal(column, row)):
                    return False
        return True

    def display(self):
        """
        Display the board with tiles
        """
        background(0, 100, 0)
        # draw line
        for i in range(1, self.BOARD_SIZE):
            strokeWeight(self.STROKEWEIGHT)
            line(0, (i * self.GRID_SIZE),
                 (self.BOARD_SIZE * self.GRID_SIZE), (i * self.GRID_SIZE))
            line((i * self.GRID_SIZE), 0,
                 (i * self.GRID_SIZE),  (self.BOARD_SIZE * self.GRID_SIZE))
        # display tiles
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if (self.tiles[i][j] != self.DEFAULT):
                    self.tiles[i][j].display()
