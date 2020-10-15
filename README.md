# Chess project in Python

## Classes
The following classes will be implemented:

### Board
8 x 8 matrix.

Lower left corner is denoted a1 (black tile), upper right corner denoted h8.

Row 1 is closest to the white player, row 8 is closest to the black player.

### Piece
#### Attributes
Color: String 'WHITE' / 'BLACK'

x_pos: Column

y_pos: Row

### Pawn
#### Attributes
Inherits from `Piece`

### Knight
#### Attributes
Inherits from `Piece`

### Bishop
#### Attributes
Inherits from `Piece`

### Rook
#### Attributes
Inherits from `Piece`

has_moved: Bool

### Queen
#### Attributes
Inherits from `Piece`

### King
#### Attributes
Inherits from `Piece`

has_moved: Bool (default False)

checked: Bool (default False)

## Methods
### `check_castling(board, king, rook)`
Checks if castling, *rokade*, is possible.

Returns boolean, `True` if neither king nor rook
has moved, and the row between them is free of other pieces.