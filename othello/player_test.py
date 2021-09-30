from player import Player
from board import Board
from game_manager import GameManager
from human_player import HumanPlayer
from ai_player import AiPlayer
from tile import Tile


def test_get_occupied_positions():
    board = Board(8)
    p = Player(board, "black")
    board.set_initial_tiles()
    occupied = p.get_occupied_positions()
    assert occupied == {(3, 3), (3, 4), (4, 3), (4, 4)}


def test_adjacent_positions_check_initial_tile_outline():
    board = Board(8)
    p = Player(board, "black")
    board.set_initial_tiles()
    outline, occupied = p.adjacent_positions()
    outline_set = {(2, 4), (5, 5), (5, 4),
                   (4, 2), (2, 3), (4, 5), (2, 2), (5, 3),
                   (3, 2), (2, 5), (3, 5), (5, 2)}
    assert outline == outline_set


def test_adjacent_positions_check_5_tiles():
    board = Board(8)
    p = Player(board, "black")
    board.set_initial_tiles()
    p.create_tile(3, 2)
    outline, occupied = p.adjacent_positions()
    outline_set = {(1, 2), (1, 3), (1, 4), (2, 4),
                   (5, 5), (5, 4), (4, 2), (4, 5), (2, 2),
                   (5, 3), (3, 2), (2, 5), (3, 5), (5, 2)}
    assert outline == outline_set


def test_between_two_point():
    board = Board(8)
    p = Player(board, "black")
    empty_list = p.between_two_point(3, 3, 4, 5)
    assert empty_list == []
    list_between = p.between_two_point(4, 4, 6, 2)
    assert list_between == [(5, 3)]
    assert p.between_two_point(0, 0, 0, 3) == [(0, 1), (0, 2)]


def test_legal_positions():
    board = Board(4)
    board.set_initial_tiles()
    player = Player(board, "black")
    legal_position = player.legal_positions()
    assert legal_position == {(0, 1), (1, 0), (3, 2), (2, 3)}
    large_board = Board(8)
    player2 = Player(large_board, "black")
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[4][4] = Tile(4, 4, "white")
    large_board.tiles[4][3] = Tile(3, 4, "white")
    assert player2.legal_positions() == {(5, 4), (5, 5), (3, 5), (5, 2)}


def test_check_legal():
    board = Board(4)
    board.set_initial_tiles()
    p = Player(board, "black")
    assert p.check_legal(1, 0) is True
    assert p.check_legal(2, 2) is False
    assert p.check_legal(1, 3) is False
    large_board = Board(8)
    player2 = Player(large_board, "black")
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[4][4] = Tile(4, 4, "white")
    large_board.tiles[4][3] = Tile(3, 4, "white")
    assert player2.check_legal(5, 5) is True
    assert player2.check_legal(5, 6) is False


def test_create_tile():
    board = Board(4)
    board.set_initial_tiles()
    p = Player(board, "black")
    p.create_tile(0, 1)
    assert board.tiles[1][0].color == "black"
    large_board = Board(8)
    player2 = Player(large_board, "black")
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[4][4] = Tile(4, 4, "white")
    large_board.tiles[4][3] = Tile(3, 4, "white")
    player2.create_tile(5, 5)
    assert large_board.tiles[5][5].color == "black"


def test_flip():
    large_board = Board(8)
    player2 = Player(large_board, "black")
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[4][4] = Tile(4, 4, "white")
    large_board.tiles[4][3] = Tile(3, 4, "white")
    player2.flip(5, 5)
    assert large_board.tiles[4][4].color == "black"


def test_flip_4x4():
    board = Board(4)
    board.set_initial_tiles()
    p = Player(board, "black")
    p.flip(1, 0)
    assert board.tiles[1][1].color == "black"
    board = Board(4)
    board.set_initial_tiles()
    p = Player(board, "white")
    p.flip(2, 0)
    assert board.tiles[1][2].color == "white"
