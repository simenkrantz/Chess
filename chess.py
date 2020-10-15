#!/usr/bin/python3
import numpy as np
import math

class Board():
    def __init__(self, num_rows = 8, num_cols = 8):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.board = np.ones(shape=(self.num_rows, self.num_cols))

        # TODO
        #   Init board layout
        #   

    def show_board(self):
        s = [[str(e) for e in row] for row in self.board]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = ''.join('\t{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n\n\n'.join(table)

class Piece():
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, board, new_x, new_y):
        
        self.x_pos = new_x
        self.y_pos = new_y

class Pawn(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)


class Knight(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)


class Bishop(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)


class Rook(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.has_moved = False

    def move(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y
        self.has_moved = True


class Queen(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)


class King(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.has_moved = False
        self.checked = False

    def move(self, new_x, new_y):

        # TODO
        #   Check that the new position
        #   isn't threatened by a piece of 
        #   the opposite color

        self.x_pos = new_x
        self.y_pos = new_y
        self.has_moved = True



def check_castling(board, king, rook):
    """Check if a castling, O-O or O-O-O, is possible.

    Parameter:
        board:  Board object
        king:   King object
        rook:   Rook object
    
    @return: Bool
    """
    assert (king.color == rook.color), "Pieces are of different colors"
    assert (not king.has_moved), "The king has moved"
    assert (not rook.has_moved), "The rook has moved"

    # TODO:
    #   Loop over the board row and check that all tiles
    #   are free for other pieces

    pass


if __name__ == "__main__":
    board = Board()
    board.show_board()