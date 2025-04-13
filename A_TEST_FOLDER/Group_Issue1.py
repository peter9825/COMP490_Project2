import sys
import os

# Add the parent directory to Python's path.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now this should import from your local version
import chess
from chess import (
    BaseBoard, QUEEN, PAWN, KNIGHT, BLACK, WHITE
)
# Verify which module is being used
print(f"Chess module location: {chess.__file__}")

board = BaseBoard()

# Counts all pieces on the board.
total_pieces = board.count_pieces()

# Counts pieces by color.
black_pieces = board.count_pieces(color=BLACK)
white_pieces = board.count_pieces(color=WHITE)

# Counts pieces by type.
queen_pieces = board.count_pieces(piece_type=QUEEN)
knight_pieces = board.count_pieces(piece_type=KNIGHT)
pawn_pieces = board.count_pieces(piece_type=PAWN)

# Counts pieces by color & type.
black_queen_pieces = board.count_pieces(color=BLACK, piece_type=QUEEN)
white_knight_pieces = board.count_pieces(color=WHITE, piece_type=KNIGHT)
black_pawn_pieces = board.count_pieces(color=BLACK, piece_type=PAWN)

print("Chess Board Analysis")
print("-------------------")
print(f"Total pieces on the board: {total_pieces}")
print("\nPieces by Color:")
print(f"  White pieces: {white_pieces}")
print(f"  Black pieces: {black_pieces}")
print("\nPieces by Type:")
print(f"  Queens: {queen_pieces}")
print(f"  Knights: {knight_pieces}")
print(f"  Pawns: {pawn_pieces}")
print("\nPieces by Color & Type:")
print(f"  Black queens: {black_queen_pieces}")
print(f"  White knights: {white_knight_pieces}")
print(f"  Black pawns: {black_pawn_pieces}")
