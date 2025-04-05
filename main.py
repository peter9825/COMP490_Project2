"""
A simple proof of concept script for the python-chess library.
This demonstrates basic functionality like board creation, move making,
and checking game states.
"""
import chess

def main(): 
    # Create a new chess board in the starting position
    board = chess.Board()

    print("Initial board state:")
    print(board)
    print(f"Total pieces: {board.count_pieces()}")
    print()

    # Demonstrate some basic functionality
    print(f"Is checkmate: {board.is_checkmate()}")
    print(f"Is stalemate: {board.is_stalemate()}")
    print(f"Is check: {board.is_check()}")
    print(f"FEN: {board.fen()}")
    print()

    # Make a few moves (e4, e5, Qh5, Nc6, Bc4, Nf6, Qxf7#) - Scholar's mate
    moves = ["e2e4", "e7e5", "d1h5", "b8c6", "f1c4", "g8f6", "h5f7"]

    print("Playing the Scholar's mate sequence:")
    for move_uci in moves:
        move = chess.Move.from_uci(move_uci)
        board.push(move)
        print(f"After {move_uci}:")
        print(board)
        print(f"Total pieces: {board.count_pieces()}")
        print()

    # Check the final position
    print(f"Is checkmate: {board.is_checkmate()}")
    print(f"Is stalemate: {board.is_stalemate()}")
    print(f"Is check: {board.is_check()}")
    print(f"FEN: {board.fen()}")
    print()

    # Show legal moves in a position
    board = chess.Board()
    board.push_san("e4")
    print("Board after e4:")
    print(board)
    print(f"Total pieces: {board.count_pieces()}")
    print()

    print("Legal moves:")
    for move in board.legal_moves:
        print(f" - {move} ({board.san(move)})")

if __name__ == "__main__":
    main()
