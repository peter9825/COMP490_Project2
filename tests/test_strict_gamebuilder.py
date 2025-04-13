import unittest
import chess
import io
import chess.pgn
from chess.pgn import StrictGameBuilder

VALID_PGN = """\
    [Event "Test Event"]
    [Site "Nowhere"]
    [Date "2020.01.01"]
    [Round "1"]
    [White "Player1"]
    [Black "Player2"]
    [Result "*"]

    1. e4 e5 *
"""

INVALID_PGN = """\
[Event "Test Event"]
[Site "Nowhere"]
[Date "2020.01.01"]
[Round "1"]
[White "Player1"]
[Black "Player2"]
[Result ""]

    1. e9e5


"""

class TestStrictGameBuilder(unittest.TestCase):
    def test_valid_pgn(self):
        """Tests that a correctly formatted pgn file is passed correctly."""
        pgn_file = io.StringIO(VALID_PGN)
        game = chess.pgn.read_game(pgn_file, Visitor=StrictGameBuilder)

        self.assertIsNotNone(
            game, "StrictGameBuilder failed to parse a valid PGN."
        )

        self.assertEqual(
            len((game.errors)), 0, "Number of game errors should be 0."
        )

class TestInvalidPGN(unittest.TestCase):
    def test_invalid_move(self):
        pgn_file = io.StringIO(INVALID_PGN)

        with self.assertRaises(Exception) as cm:
            chess.pgn.read_game(pgn_file, Visitor=StrictGameBuilder)

        self.assertIn("illegal san", str(cm.exception).lower())

if __name__ == "__main__":
    unittest.main()
