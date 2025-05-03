"""
Proof-of-Concept for lenient vs strict PGN parsing.

Run with:
    python main.py
"""
import io
import logging
import chess.pgn
from chess.pgn import StrictGameBuilder

# Make all parser logs visible
logging.basicConfig(level=logging.DEBUG)

malformed_pgn = """\
[Event "Test"]
[Site "Here"]
[Date "2025.01.01"]
[Round "1"]
[White "W"]
[Black "B"]
[Result "*"]

1. e9e5 e4 *
"""

# parse with default handle_error method, logs errors to a list instead of raising them
def parse_lenient():
    game = chess.pgn.read_game(io.StringIO(malformed_pgn))
    print("Lenient caught:", game.errors)
    

def parse_strict_via_flag():
    chess.pgn.read_game(io.StringIO(malformed_pgn), strict_errors=True)
   
def parse_strict_via_class():
    chess.pgn.read_game(io.StringIO(malformed_pgn), Visitor=StrictGameBuilder)
   

if __name__ == "__main__":
    print("=== Lenient ===")
    parse_lenient()

    print("\n=== Strict via flag ===")
    try:
        parse_strict_via_flag()
    except Exception as e:
        print("Strict(flag) correctly raised:", e)

    print("\n=== Strict via class ===")
    try:
        parse_strict_via_class()
    except Exception as e:
        print("Strict(class) correctly raised:", e)