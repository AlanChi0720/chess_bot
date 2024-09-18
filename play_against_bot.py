import chess
import chess.engine


FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
GAME_IS_ON = True
engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-sse41-popcnt.exe")
board = chess.Board(FEN)


def format_moves(pv):
    return [move.uci() for move in pv]

def computer_move():
    global GAME_IS_ON
    info = engine.analyse(board, chess.engine.Limit(depth=14), multipv=1)
    pv = info[0]["pv"]
    move = pv[0]
    if move in board.legal_moves:
        print(move)
        board.push(move)
        if board.is_game_over():
            GAME_IS_ON = False
            print(f"Game is over, computer wins!")

def ask_valid_move(player):
    global GAME_IS_ON
    print(board)
    print(f"Please use UCI to input the move for {player}:")
    move_str = input(f"{player}: ").lower()
    try:
        move = chess.Move.from_uci(move_str)
        if move in board.legal_moves:
            board.push(move)
            if board.is_game_over():
                GAME_IS_ON = False
                print(f"Game is over, {player} wins!")
        else:
            print("Invalid move. Please try again.")
    except ValueError:
        print("Invalid move notation. Please try again.")

    



player = input("Please choose W or B: ").lower()     

if player == "w":
    player = "White"
else:
    player = "Black"
    computer_move()  # Computer makes the first move if player chooses Black

while GAME_IS_ON:
    if player == "White":
        ask_valid_move("White")
        if GAME_IS_ON:
            computer_move()
    else:
        if GAME_IS_ON:
            ask_valid_move("Black")
            computer_move()


engine.quit()