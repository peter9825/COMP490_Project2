import unittest
import io
import chess
import chess.pgn

class TestExtractPositions(unittest.TestCase):
    
    def setUp(self):
        # standard test PGN
        self.test_pgn_str = '''
[Event "Test Game"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "Player1"]
[Black "Player2"]
[Result "*"]

1. e4 c5 { Sicilian } { [%csl Gd4][%cal Gc5d4] } 2. Nf3 (2. Nc3 { Closed Sicilian } 2... d6) 2... d6 3. d4 cxd4 4. Nxd4 Nf6 *
'''
        
        # empty PGN with just headers
        self.empty_pgn_str = '''
[Event "Empty Game"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "Player1"]
[Black "Player2"]
[Result "*"]

*
'''
        
        # PGN with custom starting position
        self.custom_position_pgn_str = '''
[Event "Custom Position"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "Player1"]
[Black "Player2"]
[Result "*"]
[FEN "r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3"]
[SetUp "1"]

3. d4 cxd4 4. Nxd4 Nf6 *
'''

    def test_happy_path(self):
        """Test the basic functionality with a standard PGN"""
        pgn = io.StringIO(self.test_pgn_str)
        game = chess.pgn.read_game(pgn)
        
        positions_black = game.extract_positions(repertoire_color='black')
        
        self.assertEqual(len(positions_black), 5, "Should extract 5 positions for black's repertoire")
        
        for fen, move_text in positions_black:
            self.assertIsInstance(fen, str)
            self.assertIsInstance(move_text, str)
            
        positions_white = game.extract_positions(repertoire_color='white')
        
        self.assertEqual(len(positions_white), 5, "Should extract 5 positions for white's repertoire")

    def test_empty_game(self):
        """Test with a game that has no moves"""
        pgn = io.StringIO(self.empty_pgn_str)
        game = chess.pgn.read_game(pgn)
        
        positions_black = game.extract_positions(repertoire_color='black')
        positions_white = game.extract_positions(repertoire_color='white')
        
        self.assertEqual(len(positions_black), 0, "Should extract 0 positions from an empty game")
        self.assertEqual(len(positions_white), 0, "Should extract 0 positions from an empty game")

    def test_invalid_color(self):
        """Test with an invalid repertoire color"""
        pgn = io.StringIO(self.test_pgn_str)
        game = chess.pgn.read_game(pgn)
        
        with self.assertRaises(ValueError):
            game.extract_positions(repertoire_color='invalid')

if __name__ == '__main__':
    unittest.main()