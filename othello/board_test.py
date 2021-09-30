from board import Board
from tile import Tile


def test_constructor():
    board = Board(0)
    assert board.tiles == []
    board = Board(2)
    assert board.tiles == [[0, 0], [0, 0]]
    board = Board(4)
    assert board.tiles == [[0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0]]


def test_set_initial_tiles():
    board = Board(0)
    board.set_initial_tiles()
    assert board.tiles == []
    board = Board(2)
    board.set_initial_tiles()
    assert board.tiles[0][0].color == "white"
    assert board.tiles[1][1].color == "white"
    assert board.tiles[0][1].color == "black"
    assert board.tiles[1][0].color == "black"
    board = Board(4)
    board.set_initial_tiles()
    assert board.tiles[1][1].color == "white"
    assert board.tiles[2][2].color == "white"
    assert board.tiles[2][1].color == "black"
    assert board.tiles[1][2].color == "black"
    assert board.tiles == [[0, 0, 0, 0], [0, 'white', 'black', 0],
                           [0, 'black', 'white', 0], [0, 0, 0, 0]]


def test_change_turn():
    board = Board(4)
    assert board.current_color == "black"
    board.change_turn()
    assert board.current_color == "white"


def test_white_num():
    board = Board(4)
    board.tiles[0][0] = Tile(0, 0, "white")
    assert board.white_num == 1


def test_black_num():
    board = Board(4)
    board.tiles[0][0] = Tile(0, 0, "black")
    assert board.black_num == 1


def test_create_tile():
    board = Board(4)
    board.create_tile(0, 0)
    assert board.tiles[0][0].color == "black"
    board.create_tile(1, 1)
    assert board.tiles[1][1].color == "white"


def test_check_legal():
    board = Board(4)
    assert board.check_legal(0, 0) is True
    board.create_tile(0, 0)
    assert board.check_legal(0, 0) is False


def test_check_filled():
    board = Board(4)
    assert board.check_filled() is False
    for i in range(4):
        for j in range(4):
            board.create_tile(i, j)
    assert board.check_filled() is True
