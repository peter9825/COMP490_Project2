import unittest
import chess
import io
from chess.pgn import (read_all_headers)


test_pgn_happy_path = """
[Event "Test Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "1"]
[White "Player A"]
[Black "Player B"]
[Result "1-0"]

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O 1-0

[Event "Test Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "2"]
[White "Player C"]
[Black "Player D"]
[Result "0-1"]

1. d4 d5 2. c4 e6 3. Nc3 Nf6 0-1

[Event "Test Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "3"]
[White "Player E"]
[Black "Player F"]
[Result "1/2-1/2"]

1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 a6 1/2-1/2
"""

test_pgn_edge_cases = """
[Event "Edge Case Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "1"]
[White "Player A"]
[Black "Player B"]
[Result "1-0"]

{ This game has a comment before any moves }
1. e4 e5 2. Nf3 Nc6 3. Bb5 1-0


[Event "Edge Case Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "2"]
[White "Player C"]
[Black "Player D"]
[Result "0-1"]

{ This game has empty movetext }

0-1


[Event "Edge Case Tournament"]
[Site "Test City"]
[Date "2024.04.18"]
[Round "3"]
[White "Player E"]
[Black "Player F"]
[Result "1/2-1/2"]
[Empty ""]

{ This game has multiple blank lines before and after it }



1. e4 c5 2. Nf3 1/2-1/2


[Event "Edge Case Tournament"]
[Site "Test City"]
[Round "4"]
[White "Player G"]
[Black "Player H"]
[Result "*"]

{ This game has incomplete headers (missing Date) and unfinished result }
1. e4 e5 *



[Event ""]
[Site ""]
[Date ""]
[Round ""]
[White ""]
[Black ""]
[Result ""]

{ This game has empty headers that should still be counted since there are values, just empty }
1. e4 *
"""

# test to make sure that all games are counted, no empty headers are counted.
class TestParsePgn(unittest.TestCase):

    def test_happy_path_header_count(self):
        """
        Ensure we parse exactly 3 header blocks (one per game).
        """
        stream = io.StringIO(test_pgn_happy_path)
        headers_list = list(read_all_headers(stream))
        self.assertEqual(
            len(headers_list),
            3,
            f"Expected 3 header sections, got {len(headers_list)}"
        )

    def test_pgn_edge_cases(self):
        stream = io.StringIO(test_pgn_edge_cases)
        headers_list = list(read_all_headers(stream))
        self.assertEqual(
            len(headers_list),
            5,
            f"Expected 5 header sections, got {len(headers_list)}"
        )

if __name__ == "__main__":
    unittest.main()
