"""
Proof-of-Concept for testing StrictGameBuilder.

This script creates an intentionally malformed PGN game and then parses it
using both the default GameBuilder (which suppresses errors) and the strict
version (StrictGameBuilder) that raises errors immediately.

Run this file with:
    python main.py
"""

import io
import chess.pgn
import logging
from chess.pgn import StrictGameBuilder

# Configure logging so that engine/PGN parsing logs are visible during testing.
logging.basicConfig(level=logging.DEBUG)
# Define a deliberately malformed PGN string.
# For instance, the move "e9e5" is invalid because there is no square "e9".
malformed_pgn = """\
[Event "Test Event"]
[Site "Nowhere"]
[Date "2020.01.01"]
[Round "1"]
[White "Player1"]
[Black "Player2"]
[Result "*"]

1. e9e5 *
"""

def parse_with_default():
    """
    Parse the malformed PGN using the default GameBuilder.
    This parser logs errors and adds them to the game.errors list
    rather than raising them.
    """
    # Create an in‑memory file with the malformed PGN.
    pgn_file = io.StringIO(malformed_pgn)
    game = chess.pgn.read_game(pgn_file)
    # Print the outcome: it should complete without raising an exception,
    # but with errors stored in game.errors.
    if game.errors:
        print("Default GameBuilder caught errors:")
        for error in game.errors:
            print(" -", error)
    else:
        print("Default GameBuilder did not catch any errors (unexpected).")

def parse_with_strict():
    """
    Parse the malformed PGN using StrictGameBuilder,
    which is a subclass of GameBuilder that raises errors immediately.
    """
    # Import the strict builder from the library.
    # (Assumes that StrictGameBuilder was added to chess.pgn.)

    pgn_file = io.StringIO(malformed_pgn)
    # This call should raise an exception because of the malformed move.
    game = chess.pgn.read_game(pgn_file, Visitor=StrictGameBuilder)
    # If no exception is raised, print an error (this is not expected).
    print("StrictGameBuilder did not raise an error as expected.")

def main():
    print("Parsing with default (lenient) GameBuilder:")
    try:
        parse_with_default()
    except Exception as ex:
        print("Default GameBuilder raised an exception unexpectedly:", ex)

    print("\nParsing with StrictGameBuilder (errors should raise exceptions):")
    try:
        parse_with_strict()
    except Exception as ex:
        # This is the expected behavior.
        print("StrictGameBuilder correctly raised an exception:")
        print(" -", ex)


if __name__ == '__main__':
    main()
