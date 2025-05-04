import unittest
import chess

class TestBoardHeaders(unittest.TestCase):
    def test_gridlines(self):
        """
        Test that when gridlines are enabled, the string representation of the board
        contains row headers and column headers.
        """
        board = chess.Board()
        board_str = board.__str__(gridlines=True)
        
        expected_column_headers = "  | a b c d e f g h\n- + ---------------\n"
        
        self.assertTrue(
            board_str.startswith(expected_column_headers),
            "When gridlines are enabled, the board string starts with the row headers."
        )
        
        self.assertIn("8 | ", board_str, "Expected row header '8 | ' not found.")
        self.assertIn("7 | ", board_str, "Expected row header '7 | ' not found.")
        self.assertIn("1 | ", board_str, "Expected row header '1 | ' not found.")

    def test_gridlines_disabled(self):
        """
        Test that when gridlines are disabled, the string representation of 
        the board does not contain the row or column headers.
        """
        board = chess.Board()
        board_str = board.__str__(gridlines=False)
        
        self.assertFalse(
            board_str.startswith("  | a b c d e f g h"),
            "When gridlines are disabled, the board string does not include the column headers."
        )
        
        self.assertNotIn("8 | ", board_str, "Row headers are not present when gridlines are disabled.")

    def test_empty_board_gridlines(self):
        """
        Test gridlines on an empty board to verify proper format is maintained.
        """
        board = chess.Board(None)
        board_str = board.__str__(gridlines=True)
        
        self.assertTrue(
            board_str.startswith("  | a b c d e f g h"),
            "Column headers should be present on empty board with gridlines."
        )
        
        expected_empty_row = ". . . . . . . ."

        empty_row_count = sum(1 for line in board_str.split('\n') if expected_empty_row in line)
        self.assertEqual(empty_row_count, 8, "Expected 8 empty rows in empty board with gridlines.")

    def test_line_count_consistency(self):
        """
        Test that the string representation with gridlines has the expected number of lines.
        """
        board = chess.Board()
        board_str = board.__str__(gridlines=True)
        
        lines = board_str.strip().split('\n')
        self.assertEqual(len(lines), 10, "Board with gridlines should have 10 lines.")
        
        board_str_no_grid = board.__str__(gridlines=False)
        lines_no_grid = board_str_no_grid.strip().split('\n')
        self.assertEqual(len(lines_no_grid), 8, "Board without gridlines should have 8 lines.")

    def test_unicode_representation(self):
        """
        Test that unicode representation of the board works correctly.
        """
        board = chess.Board()

        board_unicode = board.unicode()
        
        self.assertIn("♜", board_unicode, "Expected to find unicode rook.")
        self.assertIn("♞", board_unicode, "Expected to find unicode knight.")
        self.assertIn("♝", board_unicode, "Expected to find unicode bishop.")

    def test_board_after_moves_gridlines(self):
        """
        Test gridlines after making some moves to ensure consistency.
        """
        board = chess.Board()

        board.push_san("e4")
        board.push_san("e5")
        board.push_san("Nf3")
        
        board_str = board.__str__(gridlines=True)
        
        self.assertTrue(
            board_str.startswith("  | a b c d e f g h"),
            "Column headers should be present after moves."
        )
        
        self.assertIn("5 | . . . . P . . .", board_str, "White pawn should be at e4 (shown on rank 5).")
        self.assertIn("4 | . . . . p . . .", board_str, "Black pawn should be at e5 (shown on rank 4).")
        self.assertIn("8 | R N B Q K B . R", board_str, "White rook should be on first rank.")
        self.assertIn("6 | . . . . . N . .", board_str, "White knight should be at f3 (shown on rank 6).")

    def test_edge_case_full_board(self):
        """
        Test a crowded board with many pieces to ensure gridlines remain aligned.
        """
        fen = "8/8/n1n1n1n1/1b1b1b1b/8/q1q1q1q1/2P2P2/RNBQKBNR w KQkq - 0 1"
        board = chess.Board(fen)
        board_str = board.__str__(gridlines=True)
        
        self.assertTrue(
            board_str.startswith("  | a b c d e f g h"),
            "Column headers should be present on crowded board."
        )
        
        row_headers = ["8 | ", "7 | ", "6 | ", "5 | ", "4 | ", "3 | ", "2 | ", "1 | "]
        for header in row_headers:
            self.assertIn(header, board_str, f"Row header {header} missing in crowded board output.")
            
        lines = board_str.strip().split('\n')
        line_lengths = [len(line) for line in lines[2:10]]  # Skip headers and separator
        self.assertEqual(min(line_lengths), max(line_lengths), 
                        "All row lines should have the same length for proper alignment.")

    def test_gridlines_consistency_across_calls(self):
        """
        Test that multiple calls to __str__ with gridlines produce consistent results.
        """
        board = chess.Board()
        
        board_str1 = board.__str__(gridlines=True)
        board_str2 = board.__str__(gridlines=True)
        
        self.assertEqual(board_str1, board_str2, 
                        "Multiple calls to __str__ with gridlines should produce identical results.")
        
        board.push_san("e4")
        board_str3 = board.__str__(gridlines=True)
        
        self.assertNotEqual(board_str1, board_str3, 
                           "Board string should change after making a move.")
        
        board_str4 = board.__str__(gridlines=True)
        self.assertEqual(board_str3, board_str4, 
                        "Multiple calls after a move should still be consistent.")

    def test_gridlines_all_rows_present(self):
        """
        Test that all row numbers are present in the gridlines output.
        """
        board = chess.Board()
        board_str = board.__str__(gridlines=True)
        
        for row_num in range(1, 9):
            self.assertIn(f"{row_num} | ", board_str, 
                          f"Row header {row_num} should be present in gridlines output.")

if __name__ == "__main__":
    unittest.main()