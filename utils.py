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

def get_key():
    """Catching keyboard presses.
    
    Credited: https://www.jonwitts.co.uk/archives/896"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


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

    for col in range(king.x_pos, rook.x_pos):
        if board[col, king.y_pos] is not None:
            return False
    return True
