#!/usr/bin/python3
# Simen Krantz Knudsen, 15.10.2020

class Piece(object):
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color

    def move(self, board, new_x, new_y):
        """Run after check_legal_move, if True then the piece can move"""
        if isinstance(self, King) or isinstance(self, Rook):
            self.has_moved = True

        board[self.x_pos, self.y_pos] = None
        self.x_pos = new_x
        self.y_pos = new_y


class Pawn(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)

    def check_legal_move(self, board, new_x, new_y):
        #
        # TODO
        #   Handle input outside the 8 x 8 board!

        tile = board[new_x, new_y]
        if self.color == tile.color:
            return False

        elif self.color == 'WHITE':
            # White pawns can only go downwards
            if new_y == self.y_pos + 1:
                if new_x == self.x_pos and tile is None:
                    return True
                elif new_x == self.x_pos + 1 and tile.color == 'BLACK':
                    return True
                elif new_x == self.x_pos - 1 and tile.color == 'BLACK':
                    return True

        elif self.color == 'BLACK':
            # Black pawns can only go upwards
            if new_y == self.y_pos - 1:
                if new_x == self.x_pos and tile is None:
                    return True
                elif new_x == self.x_pos + 1 and tile.color == 'WHITE':
                    return True
                elif new_x == self.x_pos - 1 and tile.color == 'WHITE':
                    return True
        return False


class Knight(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)

    def check_legal_move(self, new_x, new_y):
        # TODO
        pass


class Bishop(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)

    def check_legal_move(self, new_x, new_y):
        # TODO
        pass


class Rook(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.has_moved = False

    def check_legal_move(self, new_x, new_y):
        if new_x != self.x_pos and new_y != self.y_pos:
            return False
        if new_x == self.x_pos:
            #TODO
            # Moving along the current column
            pass
        elif new_y == self.y_pos:
            #TODO
            # Moving along the current row
            pass


class Queen(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)

    def check_legal_move(self, new_x, new_y):
        # TODO
        pass


class King(Piece):
    def __init__(self, x_pos, y_pos, color):
        super().__init__(x_pos, y_pos, color)
        self.has_moved = False
        self.checked = False

    def check_legal_move(self, new_x, new_y):
        if (new_x > self.x_pos + 1 or new_x < self.x_pos - 1 or
            new_y > self.y_pos + 1 or new_y < self.y_pos - 1):
            return False
        
        # TODO
        #   Check that the new position
        #   isn't threatened by a piece of 
        #   the opposite color

        return False
