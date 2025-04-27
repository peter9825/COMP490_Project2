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
    
    # Track processed positions to avoid duplicates
    processed = set()
    
    def format_comments(node):
        """Format all comments from a node"""
        result = ""
        for comment in node.comments:
            result += f" {{ {comment} }}"
        return result
    
    def process_game_tree(node=None, path=None):
        """Recursively process the game tree"""
        if node is None:
            node = game
        if path is None:
            path = []
        
        if node.parent:
            parent_board = node.parent.board()
            
            # We care about positions where it's the opponent's turn to move
            if parent_board.turn == perspective_color:
                fen = parent_board.fen()
                position_key = fen
                
                # Only process each unique position once for main line
                if node.is_main_variation() and position_key in processed:
                    return
                
                if node.is_main_variation():
                    processed.add(position_key)
                
                # Format move number and move
                move_number = parent_board.fullmove_number
                move = parent_board.san(node.move)
                
                # Format the move text depending on the side to move
                if parent_board.turn == chess.WHITE:
                    move_text = f"{move_number}. {move}"
                else:
                    move_text = f"{move_number}... {move}"
                
                # Add comments for the move
                move_text += format_comments(node)
                
                # Add response if available
                if node.variations:
                    response = node.variations[0]
                    response_board = node.board()
                    
                    if hasattr(response, 'move') and response.move:
                        response_move = response_board.san(response.move)
                        
                        # Format based on side to move
                        if response_board.turn == chess.WHITE:
                            move_text += f" {response_board.fullmove_number}. {response_move}"
                        else:
                            # For black's move, use the "N..." notation
                            move_text += f" {response_board.fullmove_number}... {response_move}"
                        
                        # Add comments for the response
                        move_text += format_comments(response)
                
                # Output position and moves
                print(f'[FEN "{fen}"]')
                print(move_text)
                print()
        
        # Continue down each variation
        for variation in node.variations:
            process_game_tree(variation, path + [variation.move])
    
    # Start processing
    process_game_tree()

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