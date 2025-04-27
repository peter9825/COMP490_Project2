# test_extract_positions.py
import chess
import chess.pgn
import io

# Test PGN string
test_pgn_str = '''
[Event "?"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "*"]

1. e4 c5 { Sicilian } { [%csl Gd4][%cal Gc5d4] } 2. Nf3 (2. Nc3 { Closed Sicilian } 2... d6) 2... d6 *
'''

def test_extract_positions():
    # Parse the PGN
    pgn = io.StringIO(test_pgn_str)
    game = chess.pgn.read_game(pgn)
    
    # Test black's repertoire
    print("Testing with repertoire_color='black':")
    positions = game.extract_positions(repertoire_color='black')
    
    for fen, move_text in positions:
        print(f'[FEN "{fen}"]')
        print(move_text)
        print()

if __name__ == "__main__":
    test_extract_positions()