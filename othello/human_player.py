from player import Player


class HumanPlayer(Player):
    """Human Player"""
    def __init__(self, board):
        """
        :Board board: an othello board object
        HumanPlayer constuctor
        """
        self.board = board
        self.current_color = "black"
