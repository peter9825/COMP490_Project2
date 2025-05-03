import unittest
import io
import chess
import chess.pgn
from chess.pgn import StrictGameBuilder, read_game


VALID_PGN       = """\
[Event "Test Event"]
[Site "Nowhere"]
[Date "2020.01.01"]
[Round "1"]
[White "Player1"]
[Black "Player2"]
[Result "*"]

1. e4 e5 *
"""


VALID_PGN_MULTI = """\
[Event "Multi Move"]
[Site "Chessville"]
[Date "2021.02.02"]
[Round "2"]
[White "Alice"]
[Black "Bob"]
[Result "1-0"]

1. d4 d5 2. c4 c6 3. Nc3 Nf6 1-0
"""


VALID_PGN_HEADERS_ONLY = """\
[Event "HeaderOnly"]
[Site "EmptyBoard"]
[Date "2023.04.04"]
[Round "4"]
[White "Eve"]
[Black "Frank"]
[Result "1/2-1/2"]

*
"""

# illegal SAN
INVALID_PGN = """\
[Event "Test Event"]
[Site "Nowhere"]
[Date "2020.01.01"]
[Round "1"]
[White "Player1"]
[Black "Player2"]
[Result ""]

1. e9e5 *
"""

class TestStrictGameBuilderHappyPaths(unittest.TestCase):

    def test_valid_single_move(self):
        """StrictGameBuilder should accept a minimal valid PGN."""
        pgn = io.StringIO(VALID_PGN)
        game = chess.pgn.read_game(pgn, Visitor=StrictGameBuilder)

        self.assertIsNotNone(game)
        self.assertEqual(len(game.errors), 0)

        moves = list(game.mainline_moves())
        self.assertEqual(len(moves), 2)

        # initialize board in starting position and append each move to the list
        board = game.board()
        san_moves = []
        for mv in moves:
            san_moves.append(board.san(mv))
            board.push(mv)
        self.assertEqual(san_moves, ["e4", "e5"])

    def test_valid_multiple_moves(self):
        """StrictGameBuilder should parse multiple moves correctly."""
        pgn = io.StringIO(VALID_PGN_MULTI)
        game = read_game(pgn, Visitor=StrictGameBuilder)
        self.assertIsNotNone(game)
        self.assertEqual(len(game.errors), 0)
        # should have 6 moves
        self.assertEqual(len(list(game.mainline_moves())), 6)

    def test_headers_only(self):
        """PGNs with only headers and no moves should parse cleanly."""
        pgn = io.StringIO(VALID_PGN_HEADERS_ONLY)
        game = chess.pgn.read_game(pgn, Visitor=StrictGameBuilder)
        self.assertIsNotNone(game)
        self.assertEqual(len(game.errors), 0)
        # no moves in mainline
        self.assertEqual(len(list(game.mainline_moves())), 0)


class TestStrictGameBuilderEdgeCases(unittest.TestCase):

     def test_invalid_move_raises(self):
        """Malformed SAN under StrictGameBuilder must raise."""
        pgn = io.StringIO(INVALID_PGN)
        with self.assertRaises(Exception) as cm:
            chess.pgn.read_game(pgn, Visitor=StrictGameBuilder)
        self.assertIn("illegal san", str(cm.exception).lower())

     def test_lenient_when_not_strict(self):
        """By default (strict_errors=False), invalid SAN is collected, not raised."""
        pgn = io.StringIO(INVALID_PGN)
        game = chess.pgn.read_game(pgn)  # default is lenient
        self.assertIsNotNone(game)
        self.assertGreater(len(game.errors), 0)
        # move list should be empty because parsing stopped on first error
        self.assertEqual(len(list(game.mainline_moves())), 0)

     def test_empty_stream_returns_none(self):
        """Reading from an empty stream yields None rather than an exception."""
        pgn = io.StringIO("")
        result = chess.pgn.read_game(pgn, Visitor=StrictGameBuilder)
        self.assertIsNone(result)


class TestStrictErrorFlag(unittest.TestCase):

    def test_strict_flag_equivalent_to_class(self):
        """read_game(..., strict_errors=True) should behave like StrictGameBuilder."""
        # valid PGN still works
        pgn_good = io.StringIO(VALID_PGN_MULTI)
        game1 = read_game(pgn_good, strict_errors=True)
        self.assertIsNotNone(game1)
        self.assertEqual(len(game1.errors), 0)

        
    def test_strict_flag_raises_on_invalid_pgn(self):
        """
        When strict_errors=True, any malformed PGN must raise immediately.
        """
        pgn_bad = io.StringIO(INVALID_PGN)
        with self.assertRaises(Exception) as cm:
            # The strict_errors flag should cause an exception on first error
            read_game(pgn_bad, strict_errors=True)

        # check the error message mentions an illegal SAN
        self.assertIn("illegal san", str(cm.exception).lower())
    
    def test_strict_flag_defaults_to_lenient(self):
        """By default strict_errors=False, even with explicit Visitor=GameBuilder."""
        pgn = io.StringIO(INVALID_PGN)
        # explicit non-strict visitor still collects errors
        game = read_game(pgn, Visitor=chess.pgn.GameBuilder, strict_errors=False)
        self.assertIsNotNone(game)
        self.assertGreater(len(game.errors), 0)


if __name__ == "__main__":
    unittest.main()
