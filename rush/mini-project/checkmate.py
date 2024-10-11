# This is the base class for all chess pieces.
class Piece:
    def __init__(self, name, color):
        self.name = name  # The piece's name (like 'P' for Pawn, 'R' for Rook).
        self.color = color  # The piece's color, either 'white' or 'black'.

    # Method to check if a move is valid. Each piece will have its own version of this.
    def is_valid_move(self, start, end, board):
        return False  # This is the default, overridden by each specific piece.

# Class for the Pawn piece.
class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        x1, y1 = start
        x2, y2 = end
        direction = -1 if self.color == "white" else 1  # White moves up (-1), black moves down (+1).

        # Moving straight forward.
        if y1 == y2:
            # Move one step forward.
            if x2 - x1 == direction and board[x2][y2] is None:
                return True
            # Move two steps forward (only on the pawn's first move).
            if x2 - x1 == 2 * direction and board[x2][y2] is None and board[x1 + direction][y2] is None:
                return x1 == 6 if self.color == "white" else x1 == 1

        # Moving diagonally to capture an opponent's piece.
        if abs(y2 - y1) == 1 and x2 - x1 == direction and board[x2][y2] is not None:
            return board[x2][y2].color != self.color

        return False  # Any other move is not allowed.

# Class for the Rook piece.
class Rook(Piece):
    def is_valid_move(self, start, end, board):
        x1, y1 = start
        x2, y2 = end

        # Rook moves straight, either horizontally or vertically.
        if x1 != x2 and y1 != y2:
            return False

        # Check if the path is clear.
        step_x = 1 if x2 > x1 else -1 if x2 < x1 else 0
        step_y = 1 if y2 > y1 else -1 if y2 < y1 else 0
        x, y = x1 + step_x, y1 + step_y

        # If any piece is blocking the path, the move is not valid.
        while (x, y) != (x2, y2):
            if board[x][y] is not None:
                return False
            x, y = x + step_x, y + step_y

        # Valid if the destination is empty or has an opponent's piece.
        return board[x2][y2] is None or board[x2][y2].color != self.color

# Class for the Knight piece.
class Knight(Piece):
    def is_valid_move(self, start, end, board):
        x1, y1 = start
        x2, y2 = end

        # Knight moves in an "L" shape (2 squares in one direction, 1 in another).
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        return (dx, dy) in [(2, 1), (1, 2)]

# Class for the Bishop piece.
class Bishop(Piece):
    def is_valid_move(self, start, end, board):
        x1, y1 = start
        x2, y2 = end

        # Bishop moves diagonally (same number of steps in x and y).
        if abs(x2 - x1) != abs(y2 - y1):
            return False

        # Check if the diagonal path is clear.
        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1
        for i in range(1, abs(x2 - x1)):
            if board[x1 + i * step_x][y1 + i * step_y] is not None:
                return False

        # Valid if the destination is empty or has an opponent's piece.
        return board[x2][y2] is None or board[x2][y2].color != self.color

# Class for the Queen piece.
class Queen(Piece):
    def is_valid_move(self, start, end, board):
        # Queen moves like both a Rook and a Bishop.
        rook_like = Rook(self.name, self.color).is_valid_move(start, end, board)
        bishop_like = Bishop(self.name, self.color).is_valid_move(start, end, board)
        return rook_like or bishop_like  # The move is valid if it's like a Rook or Bishop move.

# Class for the King piece.
class King(Piece):
    def is_valid_move(self, start, end, board):
        x1, y1 = start
        x2, y2 = end

        # King moves one square in any direction.
        return abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1

# Class representing the chessboard and game rules.
class ChessBoard:
    def __init__(self):
        self.board = self.create_board()  # Set up the board with pieces.
        self.turn = "white"  # White goes first.

    # Create the initial chessboard setup with all the pieces in their starting positions.
    def create_board(self):
        return [
            [Rook("r", "black"), Knight("n", "black"), Bishop("b", "black"), Queen("q", "black"),
             King("k", "black"), Bishop("b", "black"), Knight("n", "black"), Rook("r", "black")],
            [Pawn("p", "black") for _ in range(8)],  # Black pawns.
            [None] * 8, [None] * 8, [None] * 8, [None] * 8,  # Empty rows.
            [Pawn("P", "white") for _ in range(8)],  # White pawns.
            [Rook("R", "white"), Knight("N", "white"), Bishop("B", "white"), Queen("Q", "white"),
             King("K", "white"), Bishop("B", "white"), Knight("N", "white"), Rook("R", "white")]
        ]

    # Display the board in a simple way.
    def print_board(self):
        for i, row in enumerate(self.board):
            # Show each row (8-1) and '.' for empty spaces.
            row_str = f"{8 - i} " + " ".join([p.name if p else "." for p in row])
            print(row_str)
        print("  a b c d e f g h")  # Show column labels.

    # Move a piece from one square to another.
    def move(self, start, end):
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]

        # Check if the move is allowed and it's the right player's turn.
        if piece and piece.color == self.turn and piece.is_valid_move(start, end, self.board):
            # Move the piece to the new square and clear the old square.
            self.board[x2][y2], self.board[x1][y1] = piece, None
            # Switch turns after a valid move.
            self.turn = "black" if self.turn == "white" else "white"
        else:
            print("Invalid move!")

    # Convert move input like 'e2 e4' into coordinates on the board.
    def parse_move(self, move):
        try:
            start_pos, end_pos = move.split()  # Split the move into start and end.
            # Convert chess notation to board coordinates.
            x1, y1 = 8 - int(start_pos[1]), ord(start_pos[0]) - ord('a')
            x2, y2 = 8 - int(end_pos[1]), ord(end_pos[0]) - ord('a')
            return (x1, y1), (x2, y2)
        except (ValueError, IndexError):
            print("Invalid input!")  # Error message if move format is wrong.
            return None, None

# Main function to play the game.
def main():
    board = ChessBoard()  # Create a new game.
    while True:
        board.print_board()  # Show the board.
        move = input(f"{board.turn}'s move (e.g., e2 e4): ").lower()  # Get a move from the player.
        if move == "stop":  # End the game if "stop" is typed.
            break
        elif move == "reset":  # Reset the game if "reset" is typed.
            board = ChessBoard()
        else:
            start, end = board.parse_move(move)  # Convert the move into coordinates.
            if start and end:
                board.move(start, end)  # Make the move if it's valid.

if __name__ == "__main__":
    main()  # Start the game.