import chess

# Create the game board object
board = chess.Board()

# Prints out the board without the gridlines.
print(board)

print("\n")

# Prints out the board with gridlines.
print(board.__str__(gridlines=True))
