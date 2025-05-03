import unittest
import chess
from chess import (BLACK, WHITE, PAWN, KNIGHT, QUEEN) 

class TestCountPieces(unittest.TestCase):

    # Test that a board initialized in the starting position has 32 pieces.
    def test_initial_count(self):        
        board = chess.Board()
        count = board.count_pieces()
        self.assertEqual(count, 32, "The starting board should have 32 pieces.")
        print("test_initial_count passed: count =", count)

    # Test that removing pieces decreases the total piece count correctly.
    def test_removal_count(self):    
        board = chess.Board()
        
        removed_piece = board.remove_piece_at(chess.D1)
        self.assertIsNotNone(removed_piece, "The white queen should be removed.")
        # Normalize value of queen and test that the piece removed was a queen  
        self.assertEqual(removed_piece.symbol().upper(), "Q", "Expected removed piece to be a queen.")    
        count_after_white_queen = board.count_pieces()    
        self.assertEqual(count_after_white_queen, 31, "After removing the white queen, the board should have 31 pieces.")
        print("test_removal_count part 1 passed: count =", count_after_white_queen)
        
        # Remove the black queen from square d8.
        removed_piece = board.remove_piece_at(chess.D8)        
        self.assertIsNotNone(removed_piece, "The black queen should be removed.")    
        self.assertEqual(removed_piece.symbol().lower(), "q", "Expected removed piece to be a queen.")
        count_after_black_queen = board.count_pieces()
        self.assertEqual(count_after_black_queen, 30, "After removing both queens, the board should have 30 pieces.")
        print("test_removal_count part 2 passed: count =", count_after_black_queen)

        # Remove the white king from square e1.
        removed_piece = board.remove_piece_at(chess.E1)
        self.assertIsNotNone(removed_piece, "The white king should be removed.")
        self.assertEqual(removed_piece.symbol().upper(), "K", "Expected removed piece to be a king.")
        count_after_white_king = board.count_pieces()
        self.assertEqual(count_after_white_king, 29, "After removing the white king, the board should have 29 pieces.")
        print("test_removal_count part 3 passed: count =", count_after_white_king)

    # Test that an empty board (created by passing None to the constructor) has zero pieces.
    def test_empty_board(self):
        board = chess.Board(None)
        count = board.count_pieces()
        self.assertEqual(count, 0, "An empty board should have 0 pieces.")
        print("test_empty_board passed: count =", count)

    # if user selects a color and a piece it should return the number of that piece and what color they are
    def test_piece_color_board(self):
        board = chess.Board()
        count = board.count_pieces(color = WHITE, piece_type = PAWN)
        self.assertEqual(count, 8, "A full board should have 8 white pawns.")
        print("The total number of white pawns is =", count)

    # tests the number of queens on a full board
    def test_piece_board(self):
        board = chess.Board()
        count = board.count_pieces(piece_type = QUEEN)
        self.assertEqual(count, 2, "A full board should have 2 queens.")
        print("The total number of queens on a full board is =", count)

    # tests the number of black pieces on a full board
    def test_color_board(self):
        board = chess.Board()
        count = board.count_pieces(color = BLACK)
        self.assertEqual(count, 16, "A full board has 16 black pieces.")
        print("The total number of black pieces on a full board is =", count)

    # test the number of pieces within a specific board instance
    def test_board_sequence(self):
        board = chess.Board("8/8/8/8/8/8/4PP2/8 w - - 0 1") # board sequence containing only 2 white pawns
        count = board.count_pieces(piece_type = PAWN, color = WHITE)
        self.assertEqual(count, 2, "there are 2 white pawns within this board squence.")
        count = board.count_pieces(piece_type = PAWN, color = BLACK)
        self.assertEqual(count, 0, "there are 0 black pawns within this board squence.")


    def test_invalid_piece_type_raises(self):
        """Providing an invalid piece_type should raise ValueError."""
        board = chess.Board()
        with self.assertRaises(ValueError):
            board.count_pieces(piece_type=0)  # valid types are 1–6

    def test_invalid_color_raises(self):
        """Passing a color other than WHITE (0) or BLACK (1) should raise IndexError."""
        board = chess.Board()
        with self.assertRaises(IndexError):
            # occupied_co is a list of length 2, so index 2 is out of range
            board.count_pieces(color=2)
    

if __name__ == '__main__':
    unittest.main()
 