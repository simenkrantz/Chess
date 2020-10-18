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
        print(f"{bcolors.OKBLUE}Press Ctrl+C or to exit the program{bcolors.ENDC}")
        print("Columns: a -- h\t\tRows: 1 -- 8")
        print("{}".format(message_to_user))
        board.show_board()

        piece_to_move = input("\nWhich piece do you want to move? ")
        col = piece_to_move[0]      # a -- h
        row = int(piece_to_move[1]) # 1 -- 8

        if not isinstance(col, str) or not isinstance(row, int):
            print("Invalid choice. Choose again")
        else:
            print("You want to move {}".format(piece_to_move))

        time.sleep(3)
        
        os.system('clear')

        

if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        os.system('clear')
        sys.exit(0)