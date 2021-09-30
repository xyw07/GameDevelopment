from tile import Tile


class Player():
    """Game player class. This contains code that is common to
all players (human and AI) in the game."""
    def __init__(self, board, color):
        """
        :Board board: an othello board object
        Player constructor
        """
        self.board = board
        self.current_color = color  # represent the color of this player's tile

    def create_tile(self, column, row):
        """
        create a tile in a legal position
        and flip the opponent's tiles
        """
        if self.check_legal(column, row):
            self.board.create_tile(column, row)
            # the board will change turn automatically
            # print("create tile")
            self.flip(column, row)

    def check_legal(self, column, row):
        """
        check if the current position legal,
        (if it in the possible legal positions)
        return Ture if legal position exists
        """
        current_legal_positions = self.legal_positions()
        return (row, column) in current_legal_positions

    def get_occupied_positions(self):
        """
        Return a set of position (row, col) which represents the occupied tiles
        """
        occupied_positions = set()
        for row in self.board.tiles:
            for tile in row:
                if (tile != self.board.DEFAULT):
                    occupied_positions.add((tile.row, tile.column))
        return occupied_positions

    def adjacent_positions(self):
        """
        through 2D list and current turn
        determine the possible next tile legal positions
        Return the set of adjacent_positions(row,col),
        which represents the outline tiles
        of the current occupied positions
        and a set of occupied positions (row,col): the positions
        of tiles that have been placed on the board
        """
        occupied_positions = self.get_occupied_positions()
        adjacent_positions = set()
        direction_set = {(1, 0), (-1, 0),
                         (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)}
        for position_tuple in occupied_positions:
            for direct in direction_set:
                adjac_row = position_tuple[0] + direct[0]
                adjac_col = position_tuple[1] + direct[1]
                if (adjac_row >= 0 and adjac_row < self.board.BOARD_SIZE
                   and adjac_col >= 0 and adjac_col < self.board.BOARD_SIZE):
                    if (adjac_row, adjac_col) not in occupied_positions:
                        adjacent_positions.add((adjac_row, adjac_col))
        return adjacent_positions, occupied_positions

    def legal_positions(self):
        """
        Calculate all legal positions that can trigger flipping
        Return a set of tuple (row,col) represent the legal positions
        """
        adjacent_positions, occupied_positions = self.adjacent_positions()
        current_legal_positions = set()
        for ad_row, ad_col in adjacent_positions:
            for row, col in occupied_positions:
                if self.board.tiles[row][col].color == self.current_color:
                    # check if same col, row, dia
                    if(ad_row == row or ad_col == col or
                       abs(float((ad_col - col))/float((ad_row - row))) == 1):
                        between_list = \
                            self.between_two_point(ad_row, ad_col, row, col)
                        valid = False
                        for betw_row, betw_col in between_list:
                            # check if have empty space in between
                            this_poistion_tile = \
                                self.board.tiles[betw_row][betw_col]
                            if this_poistion_tile == self.board.DEFAULT:
                                valid = False
                                break
                            elif this_poistion_tile.color \
                                    == self.current_color:
                                valid = False
                                break
                            else:
                                valid = True
                                pass
                                # check if have opponent tile in between
                        if (valid):
                            current_legal_positions.add((ad_row, ad_col))
                            # only check all the between
                            # we can say this adjacent is legal
        return current_legal_positions

    def between_two_point(self, row1, col1, row2, col2):
        """
        Return a list of position in between, from point A(row1,col1)
        to point B(row2, col2)
        The two input points must be aligned
        horizobtally, vertically or diagonally.
        """
        between_list = []
        min_col = min(col1, col2)
        max_col = max(col1, col2)
        min_row = min(row1, row2)
        max_row = max(row1, row2)
        if (row1 == row2):
            for i in range(min_col+1, max_col):
                between_list.append((int(row1), int(i)))
        elif (col1 == col2):
            for i in range(min_row+1, max_row):
                between_list.append((i, col1))
        elif (max_col - min_col)/(max_row - min_row) \
                == 1:  # diagonal directions
            delta_row = row1 - row2
            delta_col = col1 - col2
            step_row = int(delta_row/abs(delta_row))
            step_col = int(delta_col/abs(delta_col))
            new_row = row2 + step_row
            new_col = col2 + step_col
            while ((new_row != row1) and (new_col != col1)):
                between_list.append((new_row, new_col))
                new_row += step_row
                new_col += step_col
        return between_list

    def flip(self, column, row):
        """
        flip the tiles between this tile(column, row)
        and other self tiles on the board
        """
        occupied_positions = self.get_occupied_positions()
        for op_row, op_col in occupied_positions:
            if self.board.tiles[op_row][op_col].color == self.current_color:
                if(op_row == row or op_col == column
                   or abs(float((op_col - column))/float((op_row - row)))
                   == 1):
                    between_list = \
                        self.between_two_point(op_row, op_col, row, column)
                    valid = False
                    for betw_row, betw_col in between_list:
                        # check if have empty space in between
                        this_poistion_tile = \
                            self.board.tiles[betw_row][betw_col]
                        if this_poistion_tile == self.board.DEFAULT:
                            valid = False
                            break
                        elif this_poistion_tile.color == self.current_color:
                            valid = False
                            break
                        else:
                            valid = True
                            pass
                            # flip
                    # pre: since it legal position,
                    # there must be one of the 3 if statement
                    if (valid):
                        for betw_row, betw_col in between_list:
                            this_poistion_tile = \
                                self.board.tiles[betw_row][betw_col]
                            this_poistion_tile.color = self.current_color
