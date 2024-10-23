import chess
import chess.engine


# Path to the Stockfish engine executable (adjust the path based on your installation)
stockfish_path = "D:\\python all collection\\deep_blue\\chess_ai\\stockfish\\stockfish.exe"

# Initialize the Stockfish engine
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

# Initialize a chess board
board = chess.Board()

def print_board(board):
    """Prints the current state of the chessboard"""
    print(board)

def suggest_move(board):
    """Suggests a move using Stockfish engine"""
    result = engine.play(board, chess.engine.Limit(time=2.0))
    return result.move

def user_move(move):
    """Processes the user's move and updates the board"""
    try:
        board.push_san(move)
        print("\nMove accepted.")
    except ValueError:
        print("Invalid move! Please enter a valid move in standard algebraic notation (e.g., e2e4).")

def main():
    print("Welcome to the AI Chess Assistant!")
    print_board(board)

    while not board.is_game_over():
        # User input for move
        move = input("Enter your move (e.g., e2e4): ")
        user_move(move)
        
        # Print board after the user's move
        print_board(board)
        
        # AI's turn to suggest a move
        ai_move = suggest_move(board)
        print(f"\nAI suggests: {ai_move}")
        
        # Make the move for AI
        board.push(ai_move)
        
        # Print board after AI move
        print_board(board)

    if board.is_checkmate():
        print("Checkmate! The game is over.")
    elif board.is_stalemate():
        print("Stalemate! The game is drawn.")
    elif board.is_insufficient_material():
        print("Draw due to insufficient material.")

# Close the engine after use
def cleanup():
    engine.quit()

if __name__ == "__main__":
    try:
        main()
    finally:
        cleanup()
