import chess
import chess.engine
import tkinter as tk
from tkinter import messagebox

# Path to the Stockfish engine executable
stockfish_path = "D:\\python all collection\\deep_blue\\chess_ai\\stockfish\\stockfish.exe"
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

board = chess.Board()

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chess Assistant")
        self.board_ui = []
        self.create_board_ui()
        self.update_board()

        # User move input
        self.move_entry = tk.Entry(self.root)
        self.move_entry.grid(row=8, column=0, columnspan=3)
        self.submit_button = tk.Button(self.root, text="Submit Move", command=self.submit_move)
        self.submit_button.grid(row=8, column=3, columnspan=3)

    def create_board_ui(self):
        """Create the 8x8 chessboard UI using labels."""
        for row in range(8):
            row_ui = []
            for col in range(8):
                label = tk.Label(self.root, width=4, height=2, font=("Helvetica", 16), relief="solid", anchor="center")
                label.grid(row=row, column=col)
                row_ui.append(label)
            self.board_ui.append(row_ui)

    def update_board(self):
        """Update the UI chessboard to match the current state of the board."""
        for row in range(8):
            for col in range(8):
                piece = board.piece_at(chess.square(col, 7 - row))
                text = piece.symbol().upper() if piece else ""
                self.board_ui[row][col].config(text=text)

    def submit_move(self):
        """Handle the user's move."""
        move = self.move_entry.get()
        try:
            board.push_san(move)
            self.move_entry.delete(0, tk.END)
            self.update_board()

            if board.is_game_over():
                self.game_over()
                return

            # AI makes a move
            ai_move = engine.play(board, chess.engine.Limit(time=2.0)).move
            board.push(ai_move)
            self.update_board()

            if board.is_game_over():
                self.game_over()

        except ValueError:
            messagebox.showerror("Invalid Move", "Please enter a valid move in standard algebraic notation (e.g., e2e4).")

    def game_over(self):
        """Handle the end of the game."""
        if board.is_checkmate():
            messagebox.showinfo("Game Over", "Checkmate! The game is over.")
        elif board.is_stalemate():
            messagebox.showinfo("Game Over", "Stalemate! The game is drawn.")
        elif board.is_insufficient_material():
            messagebox.showinfo("Game Over", "Draw due to insufficient material.")
        else:
            messagebox.showinfo("Game Over", "Game over!")
        self.root.quit()

def cleanup():
    """Cleanup the engine when the application is closed."""
    engine.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessApp(root)
    try:
        root.mainloop()
    finally:
        cleanup()
