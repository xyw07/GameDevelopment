import os.path


class GameManager:
    """Game Manager"""
    def __init__(self, board, human_player, ai_player):
        """
        :Board board: an othello board object
        :HumanPlayer human_player: a HumanPlayer object
        :AiPlayer ai_player: an AiPlayer object
        GameManager Constuctor
        """
        self.board = board
        self.human_player = human_player
        self.ai_player = ai_player

    def player_make_move(self, mouseX, mouseY):
        """is called in the Processing mousePressed()
        defined in the top level Processing sketch"""
        # call player's function
        # check if there exsits possible positions
        current_legal_positions = self.human_player.legal_positions()
        if (len(current_legal_positions) > 0):
            column = mouseX // self.board.GRID_SIZE
            row = mouseY // self.board.GRID_SIZE
            self.human_player.create_tile(column, row)
            # create success it will chanege turn otherwise not
        else:
            self.board.change_turn()

    def computer_make_move(self):
        """is executed in draw() inside an if conditional structure
        that checks to make sure that it is the computer's turn and
        that the time delay counter for the pause has run down to zero."""
        if (self.ai_player.check_ai_have_legal_move()):
            self.ai_player.create_tile()
        else:
            self.board.change_turn()

    def check_win_condiction(self):
        """
        Check Game Over
        Check if there is no place to put tile for both human and AI
        or the board is filled
        Return True if the game is over, otherwise false
        """
        return ((len(self.human_player.legal_positions()) == 0 and
                (not self.ai_player.check_ai_have_legal_move())) or
                self.board.check_filled())

    def win(self):
        """
        Return a string showing the game result, tie, or winner
        Black  # black tiles VS. White # white tiles
        """
        s = ""
        white_num = self.board.white_num
        black_num = self.board.black_num
        if (white_num == black_num):
            s += "Tie!" + '\n'
        else:
            if (black_num > white_num):
                # print("The winner is Black Tile with", black_num, "tiles")
                s += "Black win!" + '\n'
            else:
                # print("The winner is White Tile with", white_num, "tiles")
                s += "White win!" + '\n'
        s += "Black " + str(black_num) + " VS. " + "White " + str(white_num)
        return s

    def save_to_file(self, name, file_name):
        """
        Save user's name and score
        (number of black tiles on the board) in a file (file_name).
        The format is one score per line with a space
        between the user's name and their score.
        When a new high-scorer gives their name, they go first in the file.
        If the new person is not the high-scorer,
        they go at the end of the file.
        """
        if (os.path.isfile(file_name)):
            f = open(file_name, "r")
            first_line = f.readline()  # read first line
            if (first_line):
                score_break = first_line.rfind(" ")
                score = int(first_line[score_break+1:])
                if (self.board.black_num > score):
                    f.seek(0)
                    # seek(n) takes the file handle to the nth
                    # bite from the beginning.
                    orig_lines = f.readlines()
                    f = open(file_name, "w")
                    f.write(name + " " + str(self.board.black_num) + "\n")
                    f.writelines(orig_lines)
                else:
                    f = open(file_name, "a")
                    f.write(name + " " + str(self.board.black_num) + "\n")
            else:
                f = open(file_name, "w")
                f.write(name + " " + str(self.board.black_num) + "\n")
        else:
            f = open(file_name, "w")
            f.write(name + " " + str(self.board.black_num) + "\n")
