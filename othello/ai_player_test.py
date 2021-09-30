from ai_player import AiPlayer
from board import Board
from tile import Tile


def test_constructor():
    board = Board(8)
    ai = AiPlayer(board)
    assert ai.current_color == "white"
    assert ai.board == board


def test_legal_positions_4x4():
    board = Board(4)
    ai = AiPlayer(board)
    board.set_initial_tiles()
    board.current_color = "white"
    current_legal_positions, total_btw_num_posi = ai.legal_positions()
    assert current_legal_positions == {(3, 1), (1, 3), (0, 2), (2, 0)}
    assert total_btw_num_posi == {(3, 1): 1, (2, 0): 1, (0, 2): 1, (1, 3): 1}


def large_board_situation():
    large_board = Board(8)
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[4][3] = Tile(3, 4, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[6][3] = Tile(3, 6, "white")
    large_board.tiles[3][5] = Tile(5, 3, "white")
    large_board.current_color = "white"
    return large_board


def test_legal_positions_8x8():
    large_board = large_board_situation()
    ai = AiPlayer(large_board)
    current_legal_positions, total_btw_num_posi = ai.legal_positions()
    assert current_legal_positions == {(2, 3), (3, 2)}
    assert total_btw_num_posi == {(2, 3): 3, (3, 2): 2}


def test_create_tile():
    large_board = large_board_situation()
    ai = AiPlayer(large_board)
    assert ai.create_tile() == (2, 3)
    assert large_board.tiles[2][3].color == "white"


def test_check_ai_have_legal_move():
    large_board = large_board_situation()
    ai = AiPlayer(large_board)
    assert ai.check_ai_have_legal_move() is True
    empty_board = Board(4)
    ai2 = AiPlayer(empty_board)
    assert ai2.check_ai_have_legal_move() is False


def test_choose_position():
    large_board = large_board_situation()
    ai = AiPlayer(large_board)
    assert ai.choose_position() == (2, 3)
