from human_player import HumanPlayer
from board import Board


def test_constructor():
    board = Board(8)
    human = HumanPlayer(board)
    assert human.current_color == "black"
    assert human.board == board
