#!/usr/bin/python3
import numpy as np
import math
import enum

class Board():
    def __init__(self):
        self.num_rows = 8
        self.num_cols = 8

        # TODO
        #   Init board layout, 

    def show_board(self):
        print("Show chess board")


class Piece():
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color # 'WHITE' or 'BLACK'

    def move(self, new_x, new_y):
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


class Queen(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)


class King(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.has_moved = False
        self.checked = False


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