import io
import chess.pgn
from chess.pgn import (read_all_headers)


test_pgn = """
[Event "World Cup"]
[Site "Khanty-Mansiysk RUS"]
[Date "2009.11.29"]
[Round "3.4"]
[White "Li Chao2"]
[Black "Gashimov,V"]
[Result "0-1"]
[WhiteElo "2596"]
[BlackElo "2758"]
[EventDate "2009.11.21"]
[HashCode "00000000"]
[TotalPlyCount "0"]


{ Both Chinese players were late to the board for game two and were
defaulted }


0-1


[Event "World Cup"]
[Site "Khanty-Mansiysk RUS"]
[Date "2009.11.29"]
[Round "3.4"]
[White "Naiditsch,A"]
[Black "Svidler,P"]
[Result "1/2-1/2"]
[WhiteElo "2689"]
[BlackElo "2754"]
[ECO "C97"]
[Opening "Ruy Lopez"]
[Variation "closed, Chigorin defence"]
[EventDate "2009.11.21"]
[HashCode "312a25cf"]
[TotalPlyCount "121"]


1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O 8.
c3 d6 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. d5 c4 13. Nbd2 Nb7 14. Nf1 Nc5
15. Kh1 Bd7 16. Ng3 Ne8 17. Nh2 Bh4 18. Rf1 Qd8 19. Nf3 Bxg3 20. fxg3 f5
"""

def main():
    pgn_file = io.StringIO(test_pgn)

    print("Using standard read_headers (problem demonstration):")
    pgn_file.seek(0)

    standard_headers = []
    while True:
        headers = chess.pgn.read_headers(pgn_file)
        if headers is None:
            break
        standard_headers.append(headers)

    for i, headers in enumerate(standard_headers):
        print(f"Game {i+1}: {headers} (length: {len(headers) if headers else 0})")

    print("\nUsing fixed read_all_headers:")
    pgn_file.seek(0)

    fixed_headers = read_all_headers(pgn_file)

    for i, headers in enumerate(fixed_headers):
        print(f"Game {i+1}: {headers} (length: {len(headers)})")

if __name__ == "__main__":
    main()
