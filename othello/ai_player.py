from player import Player


class AiPlayer(Player):
    """AI player"""
    def __init__(self, board):
        """
        :Board board: The board Object
        AiPlayer constructor
        """
        self.board = board
        self.current_color = "white"

    def create_tile(self):
        """
        AI will choose a best place,
        if several position show the same best result,
        choose the first one.
        Create a tile in the board and
        Flipping the opponent's tiles
        Return the choosing position
        """
        position = self.choose_position()
        column, row = position[1], position[0]
        self.board.create_tile(column, row)
        self.flip(column, row)
        return position

    def check_ai_have_legal_move(self):
        """
        Check the current board, whether exsits legal move
        Return True if ai have legal move, otherwise False
        """
        current_legal_positions, total_btw_num_posi_dict = \
            self.legal_positions()
        return (len(current_legal_positions) > 0)

    def choose_position(self):
        """
        Instead of choosing a legal position randomly,
        AI will choose the position
        where he could filp the opponent's tiles as many as possible
        Return the position(row,col) that going to be chosen
        """
        current_legal_positions, total_btw_num_posi_dict = \
            self.legal_positions()
        # print("total_btw_num_posi_dict:", total_btw_num_posi_dict)
        if (len(current_legal_positions) > 0):
            maximum = max(total_btw_num_posi_dict.values())
            result = list(filter(lambda x: x[1] == maximum,
                                 total_btw_num_posi_dict.items()))
            # print("result:", result)
            best_first_item = result[0]
            best_position = best_first_item[0]
            # print("best position:", best_position)
            return best_position

    def legal_positions(self):
        """
        Calculate all legal positions
        Return a set of tuple (row,col) represent the legal positions
        and a dictionary, key: (row,col) represent the legal position,
        value: the number of tiles that can be fliiped.
        """
        adjacent_positions, occupied_positions = self.adjacent_positions()
        current_legal_positions = set()
        total_btw_num_posi = {}
        for ad_row, ad_col in adjacent_positions:
            total_between_num = 0
            for row, col in occupied_positions:
                if self.board.tiles[row][col].color == self.current_color:
                    # check if same col, row, dia
                    if(ad_row == row or ad_col == col
                       or (abs(float((ad_col - col))/float((ad_row - row)))
                           == 1)):
                        between_list = self.between_two_point(ad_row,
                                                              ad_col, row, col)
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
                            total_between_num += len(between_list)
                            current_legal_positions.add((ad_row, ad_col))
                            # only check all the between, we say this is legal
            if (total_between_num > 0):
                total_btw_num_posi[(ad_row, ad_col)] = total_between_num
        return current_legal_positions, total_btw_num_posi
