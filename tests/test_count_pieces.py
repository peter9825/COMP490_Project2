import unittest
import chess

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

if __name__ == '__main__':
    unittest.main()
 