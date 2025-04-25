import io
import unittest
import chess.pgn
from chess.pgn import SubGame, StringExporter

PGN = """
[Event "Example Game"]
[Site "Chess Demo"]
[Date "2025.04.25"]
[Round "1"]
[White "Player A"]
[Black "Player B"]
[Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. O-O Nf6 5. d3 O-O 6. Bg5 h6 7. Bh4 d6 8. h3 Be6
"""

class TestSubGame(unittest.TestCase):

    def setUp(self):
        pgn_io = io.StringIO(PGN)
        self.game = chess.pgn.read_game(pgn_io)

    def test_subgame_move_sequence(self):
        # Extract plies 3–6
        sub = SubGame.from_pgn_segment(self.game, start_pli=3, end_pli=6)

        board = sub.board()
        san_moves = []
        for move in sub.mainline_moves():
            san_moves.append(board.san(move))
            board.push(move)

        self.assertEqual(
            san_moves,
            ["Nf3", "Nc6", "Bc4", "Bc5"],
            "SubGame should contain exactly those four SAN moves"
        )

    def test_subgame_pgn_export(self):
        sub = SubGame.from_pgn_segment(self.game, start_pli=3, end_pli=6)
        # Export without headers/comments/variations so we just get the movetext:
        exporter = StringExporter(headers=False, comments=False, variations=False, columns=None)
        pgn_out = sub.accept(exporter).strip()

        # It should re‐number starting at move 2:
        expected = "2. Nf3 Nc6 3. Bc4 Bc5 1-0"
        self.assertEqual(pgn_out, expected)

    def test_invalid_range_raises(self):
        # start > end
        with self.assertRaises(ValueError):
            SubGame.from_pgn_segment(self.game, start_pli=8, end_pli=7)
        # end out of bounds
        with self.assertRaises(ValueError):
            SubGame.from_pgn_segment(self.game, start_pli=1, end_pli=42)

if __name__ == "__main__":
    unittest.main()
