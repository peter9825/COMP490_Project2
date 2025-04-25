import chess
import chess.pgn
import io
from chess.pgn import SubGame

pgn_string = """
[Event "Example Game"]
[Site "Chess Demo"]
[Date "2025.04.25"]
[Round "1"]
[White "Player A"]
[Black "Player B"]
[Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. O-O Nf6 5. d3 O-O 6. Bg5 h6 7. Bh4 d6 8. h3 Be6
"""


print("DEMO: SubGame Class for Chess PGN Segments")
print("-----------------------------------------\n")

pgn_io = io.StringIO(pgn_string)
full_game = chess.pgn.read_game(pgn_io)

print("Original Game:")
print(f"Headers: {full_game.headers}")
print("Moves:", end=" ")
board = full_game.board()
for move in full_game.mainline_moves():
    print(f"{board.san(move)}", end=" ")
    board.push(move)
print("\n")

print("Test 1: SubGame from moves 3-6")
subgame1 = SubGame.from_pgn_segment(full_game, 3, 6)
print("Headers:", subgame1.headers)
print("Starting position FEN:", subgame1.board().fen())
print("Moves:", end=" ")
board = subgame1.board()
for move in subgame1.mainline_moves():
    print(f"{board.san(move)}", end=" ")
    board.push(move)
print("\n")

print("Test 2: SubGame from moves 7-8")
subgame2 = SubGame.from_pgn_segment(full_game, 7, 8)
print("Headers:", subgame2.headers)
print("Starting position FEN:", subgame2.board().fen())
print("Moves:", end=" ")
board = subgame2.board()
for move in subgame2.mainline_moves():
    print(f"{board.san(move)}", end=" ")
    board.push(move)
print("\n")

print("Test 3: Exporting SubGame to PGN format")
exporter = chess.pgn.StringExporter(headers=True, variations=True, comments=True)
pgn_output = subgame1.accept(exporter)
print(pgn_output)
