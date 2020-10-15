#!/usr/bin/python3
# Simen Krantz Knudsen, 15.10.2020
import time, os, sys

from board import Board
from utils import bcolors, check_castling, get_key

def run_game():
    os.system('clear')
    board = Board()
    message_to_user = ""
    while True:
        print(f"{bcolors.OKBLUE}Press 'Ctrl+C' or to exit the program{bcolors.ENDC}")
        print("{}\n".format(message_to_user))
        board.show_board()

        time.sleep(3)
        os.system('clear')

        # if piece.check_legal_move(x,y):
        #   piece.move(x,y)
        



if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        os.system('clear')
        sys.exit(0)