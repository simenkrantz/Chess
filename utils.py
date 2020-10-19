#!/usr/bin/python3

# Utility methods for chess game
# Used in run.py
#
# Simen Krantz Knudsen, 15.10.2020
import time, os, sys, tty, termios
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_user_choice(player, board, new_pos = False):
    """get_user_choice(int, BOARD, new_pos) -> bool, row, col
    
    player WHITE = 0, player BLACK = 1
    new_pos for the second choice of piece

    Ask for board position, checks validity of choice.
    @return: valid_choice, row, column
    """
    piece_to_move = input("\nWhich piece do you want to choose? ")
    row = int(piece_to_move[1])
    col = map_column_to_int(str(piece_to_move[0]))
    valid = False


    # BUG
    #
    #   TypeError: 'Board' object not subscriptable
    tile = board[col, row]
    
    if valid_choice(row, col):
        if tile.color == 'WHITE' and player == 0:
            valid = True
        elif tile.color == 'BLACK' and player == 1:
            valid = True
        elif tile is None and new_pos:
            valid = True
    return (valid, row-1, col)


def valid_choice(row, col):
    """check_valid_piece(int, str) -> bool

    Checks if column and row of chosen piece is valid.
    Parameters:
        row (int): Should be between 1 and 8
        col (str): Should be between a and h
    """
    if col in ['a','b','c','d','e','f','g','h'] and row >= 1 and row <= 8:
        return True
    return False

def map_column_to_int(col):
    if col == 'a': return 0
    elif col == 'b': return 1
    elif col == 'c': return 2
    elif col == 'd': return 3
    elif col == 'e': return 4
    elif col == 'f': return 5
    elif col == 'g': return 6
    elif col == 'h': return 7

def check_castling(board, king, rook):
    """Check if a castling, O-O or O-O-O, is possible.

    Parameter:
        board:  Board object
        king:   King object
        rook:   Rook object
    
    @return: Bool
    """
    if (king.color != rook.color or king.has_moved or rook.has_moved):
        return False

    for col in range(king.x_pos, rook.x_pos):
        if board[col, king.y_pos] is not None:
            return False
    return True
