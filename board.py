#!/usr/bin/python3
# Simen Krantz Knudsen, 15.10.2020
import numpy as np

from pieces import Pawn, Knight, Bishop, Rook, Queen, King

class Board():
    """The board class.
    
    Responsible for initializing the board correctly,
    and keep track of all the moves.
    """
    def __init__(self):
        self.num_rows = 8
        self.num_cols = 8
        self.board = np.array([
            [
                Rook(0,0,'WHITE'),Knight(1,0,'WHITE'),Bishop(2,0,'WHITE'),King(3,0,'WHITE'),
                Queen(4,0,'WHITE'),Bishop(5,0,'WHITE'),Knight(6,0,'WHITE'),Rook(7,0,'WHITE')
            ],
            [Pawn(i, 1, 'WHITE') for i in range(self.num_cols)],
            [None for _ in range(self.num_cols)],
            [None for _ in range(self.num_cols)],
            [None for _ in range(self.num_cols)],
            [None for _ in range(self.num_cols)],
            [Pawn(i, 6, 'BLACK') for i in range(self.num_cols)],
            [
                Rook(0,7,'BLACK'),Knight(1,7,'BLACK'),Bishop(2,7,'BLACK'),King(3,7,'BLACK'),
                Queen(4,7,'BLACK'),Bishop(5,7,'BLACK'),Knight(6,7,'BLACK'),Rook(7,7,'BLACK')
            ],
        ])

    def show_board(self):
        """Prints the board in ASCII characters."""
        for i in range(self.num_rows):
            print(' ----'*8)
            s = ""
            for j in range(self.num_cols):
                s += '| {} '.format(self._show_piece(i, j))
            print("{}|".format(s))
        print(' ----'*8)

    def _show_piece(self, x_pos, y_pos):
        """Private. Returns a string with two characters, used in show_board"""
        piece = self.board[x_pos, y_pos]
        if isinstance(piece, Pawn): return '{}P'.format(piece.color[0])
        elif isinstance(piece, Knight): return '{}N'.format(piece.color[0])
        elif isinstance(piece, Bishop): return '{}B'.format(piece.color[0])
        elif isinstance(piece, Rook): return '{}R'.format(piece.color[0])
        elif isinstance(piece, Queen): return '{}Q'.format(piece.color[0])
        elif isinstance(piece, King): return '{}K'.format(piece.color[0])
        else: return '  '
        