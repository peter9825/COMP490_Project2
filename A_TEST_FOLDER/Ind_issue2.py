import io
import chess.pgn

# Parse a full game
pgn = io.StringIO("1. e4 e5 2. Nf3 (2. Nc3 d6) 2... d5 3. a4 a5 4. b4 b5")
game = chess.pgn.read_game(pgn)

# Extract from White’s 2nd move (ply 3) through Black’s 3rd (ply 6):
sub = game.extract_subgame(start_pli=3, end_pli=6)

# Print it:
print(sub)
# → 2. Nf3 2... d5 3. a4 a5
