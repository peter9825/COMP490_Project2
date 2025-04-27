import chess
import chess.pgn
import io

def extract_positions_with_moves(pgn_input = str, repertoire_color = str):
    # Determine the perspective
    if repertoire_color.lower() == 'black':
        perspective_color = chess.WHITE  # FEN positions before white's move
    elif repertoire_color.lower() == 'white':
        perspective_color = chess.BLACK  # FEN positions before black's move
    else:
        return ValueError(f"({repertoire_color}) is an invalid input for the repertoir_color.")
    
    # Read the PGN
    pgn = io.StringIO(pgn_input)
        
    game = chess.pgn.read_game(pgn)
    
    def format_comments(node):
        """Format all comments from a node"""
        result = ""
        for comment in node.comments:
            result += f" {{ {comment} }}"
        return result
    
    # Track already processed positions to avoid duplicates
    processed_positions = set()
    
    def process_position(node, path=None):
        if path is None:
            path = []
        
        # Skip the root node
        if node.parent is None:
            for variation in node.variations:
                process_position(variation)
            return
        
        # Get the board position before this move
        parent_board = node.parent.board()
        
        # Check if this position is from the chosen perspective
        if parent_board.turn == perspective_color:
            fen = parent_board.fen()
            
            # Skip if already processed this position with this move
            position_key = (fen, str(node.move))
            if position_key in processed_positions:
                return
            processed_positions.add(position_key)
            
            # Get move number and opponent's move
            move_number = parent_board.fullmove_number
            opponent_move = parent_board.san(node.move)
            
            # Format the move text
            if parent_board.turn == chess.WHITE:
                move_text = f"{move_number}. {opponent_move}"
            else:
                move_text = f"{move_number}... {opponent_move}"
            
            # Add comments for opponent's move
            move_text += format_comments(node)
            
            # Check if there's a response move
            if node.variations:
                response_node = node.variations[0]
                if hasattr(response_node, 'move') and response_node.move:
                    # Get the board after opponent's move
                    response_board = node.board()
                    response_move = response_board.san(response_node.move)
                    
                    # Add move number only for white's move
                    if response_board.turn == chess.WHITE:
                        move_text += f" {response_board.fullmove_number}."
                    
                    move_text += f" {response_move}"
                    
                    # Add comments for response
                    move_text += format_comments(response_node)
            
            # Output the position and moves
            print(f'[FEN "{fen}"]')
            print(move_text)
            print()
        
        # Process all variations
        for variation in node.variations:
            new_path = path + [variation.move]
            process_position(variation, new_path)
    
    # Start processing
    process_position(game)


# Test PGN string
test_pgn_str = '''
[Event "?"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "*"]

1. e4 c5 { Sicilian } { [%csl Gd4][%cal Gc5d4] } 2. Nf3 (2. Nc3 { Closed Sicilian } 2... d6) 2... d6 *
'''

# Run with test string
print("Testing with repertoire_color='black':")
extract_positions_with_moves(test_pgn_str, 'black')