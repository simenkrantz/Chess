#!/usr/bin/python3
# Simen Krantz Knudsen, 15.10.2020
import time, os, sys

from board import Board
from utils import bcolors, check_castling, valid_choice, get_user_choice

def run_game():
    os.system('clear')
    board = Board()
    message_to_user = ""

    # Player 0 = WHITE
    # Player 1 = BLACK

    player = 0

    while True:
        print(f"{bcolors.OKBLUE}Press Ctrl+C or to exit the program{bcolors.ENDC}")
        print("Columns: a -- h\t\tRows: 1 -- 8")
        print("{}".format(message_to_user))
        board.show_board()

        valid_piece, old_row, old_col = get_user_choice(player, board, new_pos=False)
        valid_new_pos, new_row, new_col = get_user_choice(player, board, new_pos=True)

        if valid_piece and valid_new_pos:
            tile = board[old_col, old_row]
            legal_move = tile.check_legal_move(board, new_col, new_row)
            print("Checked valid pieces")
            if legal_move:
                tile.move(board, new_col, new_row)

        print(valid_piece)
        print(valid_new_pos)
        time.sleep(3)
        
        os.system('clear')

        # Change player from W to B and vice versa
        player = not player
        

if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        os.system('clear')
        sys.exit(0)