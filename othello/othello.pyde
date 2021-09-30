from board import Board
from game_manager import GameManager
from human_player import HumanPlayer
from ai_player import AiPlayer


WIDTH = 800
HEIGHT = 800
BOARD_SIZE = 8
board = Board(BOARD_SIZE)
human_player = HumanPlayer(board)
ai_player = AiPlayer(board)
gm = GameManager(board, human_player, ai_player)
MAX_WAIT_TIME = 180
WAIT_TIME = MAX_WAIT_TIME
GAME_OVER = False
WELCOME = True


def setup():
    size(WIDTH, HEIGHT)
    board.set_initial_tiles()


def welcome():
    textSize(50)
    fill(255, 20, 20)
    text("You are black!", WIDTH/2 - 140, HEIGHT/2 - 50)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    global WAIT_TIME, GAME_OVER, WELCOME
    board.display()
    if (board.current_color == human_player.current_color and not GAME_OVER):
        if (WELCOME):
            welcome()
        textSize(50)
        fill(255, 20, 20)
        text("Your Turn!", WIDTH/2 - 140, HEIGHT/2)
    if (board.current_color == ai_player.current_color and not GAME_OVER):
        textSize(50)
        fill(255, 20, 20)
        # why I cannot put ai turn here not in the mouse pressed?
        text("AI Turn!", WIDTH/2 - 140, HEIGHT/2)
        # Another countdown
        WAIT_TIME -= 1
        if (WAIT_TIME == 0):
            gm.computer_make_move()
            WAIT_TIME = MAX_WAIT_TIME
    if (gm.check_win_condiction()):
        GAME_OVER = True
        WAIT_TIME -= 1
        win_words = gm.win()
        textSize(50)
        fill(255, 20, 20)
        text(win_words, WIDTH/2 - 180, HEIGHT/2 - 70)
        # input name and save it to file
        if (WAIT_TIME == 0):
            answer = input('Please enter your name')
            # Assume they enter string
            gm.save_to_file(answer, "scores.txt")
            noLoop()


def mousePressed():
    global WELCOME
    WELCOME = False
    if (board.current_color == human_player.current_color):
        gm.player_make_move(mouseX, mouseY)
    textSize(50)
    fill(255, 20, 20)
    if (board.current_color == human_player.current_color):
        text("Your Turn!", WIDTH/2 - 140, HEIGHT/2)
