from game_manager import GameManager
from board import Board
from human_player import HumanPlayer
from ai_player import AiPlayer
from tile import Tile
import tempfile
import os
from io import StringIO


def create_gm(board):
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    return gm


def create_gm_with_initial_tiles():
    board = Board(8)
    board.set_initial_tiles()
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    return gm


def test_constuctor():
    board = Board(8)
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    assert gm.board == board
    assert gm.human_player == human_player
    assert gm.ai_player == ai_player


def test_player_make_move():
    board = Board(8)
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    board.set_initial_tiles()
    gm.player_make_move(320, 210)
    assert board.tiles[2][3].color == "black"  # create tile
    assert board.tiles[3][3].color == "black"  # flip tile
    assert board.current_color == "white"  # next turn should be AI


def test_player_make_move_press_invalid_place():
    board = Board(8)
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    board.set_initial_tiles()
    gm.player_make_move(30, 210)
    assert board.tiles[2][0] == 0


def test_computer_make_move_no_legal_move():
    board = Board(4)
    board.current_color = "white"
    human_player = HumanPlayer(board)
    ai_player = AiPlayer(board)
    gm = GameManager(board, human_player, ai_player)
    gm.computer_make_move()
    assert board.tiles == [[0, 0, 0, 0], [0, 0, 0, 0],
                           [0, 0, 0, 0], [0, 0, 0, 0]]


def test_computer_make_move_legal_move():
    large_board = Board(8)
    large_board.tiles[3][3] = Tile(3, 3, "black")
    large_board.tiles[4][3] = Tile(3, 4, "black")
    large_board.tiles[5][3] = Tile(3, 5, "black")
    large_board.tiles[3][4] = Tile(4, 3, "black")
    large_board.tiles[6][3] = Tile(3, 6, "white")
    large_board.tiles[3][5] = Tile(5, 3, "white")
    large_board.current_color = "white"
    human_player = HumanPlayer(large_board)
    ai_player = AiPlayer(large_board)
    gm = GameManager(large_board, human_player, ai_player)
    gm.computer_make_move()
    assert large_board.tiles[2][3].color == "white"  # craete a tile
    assert large_board.tiles[3][3].color == "white"  # flip 3 tiles
    assert large_board.tiles[4][3].color == "white"
    assert large_board.tiles[5][3].color == "white"
    assert large_board.current_color == "black"  # change the turn


def test_win():
    gm = create_gm(Board(8))
    assert (gm.win()) == "Tie!\nBlack 0 VS. White 0"


def test_check_win_condiction():
    gm = create_gm(Board(8))
    assert gm.check_win_condiction() is True
    gm2 = create_gm_with_initial_tiles()
    assert gm2.check_win_condiction() is False


def test_save_to_file():
    path = tempfile.mkstemp()[1]
    gm = create_gm(Board(8))
    gm.save_to_file("Alice", path)
    gm2 = create_gm_with_initial_tiles()
    gm2.save_to_file("Jim", path)
    gm = create_gm(Board(8))
    gm.save_to_file("Alice", path)
    # create a board with 3 black tiles
    board = Board(8)
    t1 = Tile(0, 0, "black")
    t2 = Tile(0, 1, "black")
    t3 = Tile(0, 2, "black")
    board.tiles[0][0] = t1
    board.tiles[1][0] = t2
    board.tiles[2][0] = t3
    gm3 = create_gm(board)
    gm3.save_to_file("Tom", path)
    # test file
    try:
        contents = open(path).read()
    finally:
        os.remove(path)
    assert contents == "Tom 3\nJim 2\nAlice 0\nAlice 0\n"
