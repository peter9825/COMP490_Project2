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
        
        # The expected column header string
        expected_column_headers = "  | a b c d e f g h\n- + ---------------\n"
        
        # Check that the output has the column headers.
        self.assertTrue(
            board_str.startswith(expected_column_headers),
            "When gridlines are enabled, the board string starts with the row headers."
        )
        
        # Check that some of the expected row headers are present.
        # The headers are: ["8", "7", "6", "5", "4", "3", "2", "1"]
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
        
        # Check that the board string does not start with the column header string.
        self.assertFalse(
            board_str.startswith("  | a b c d e f g h"),
            "When gridlines are disabled, the board string does not include the column headers."
        )
        
        # check that row headers are also not present.
        self.assertNotIn("8 | ", board_str, "Row headers are not present when gridlines are disabled.")

if __name__ == "__main__":
    unittest.main()