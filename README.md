# Chess Game vs AI

This Python script allows you to play chess against an AI opponent powered by the Stockfish engine. The game is played in the console using UCI (Universal Chess Interface) notation for moves.

## Requirements

- Python 3.x
- `chess` library
- `chess.engine` module
- Stockfish chess engine

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python libraries:
   ```
   pip install chess
   ```
3. Download the Stockfish chess engine appropriate for your operating system from the [official Stockfish website](https://stockfishchess.org/download/).
4. Place the Stockfish executable in a directory named "stockfish" in the same folder as the script.

## Usage

1. Run the script:
   ```
   python play_against_bot.py
   ```
2. Choose your color by entering 'W' for White or 'B' for Black when prompted.
3. If you chose Black, the AI will make the first move.
4. Enter your moves in UCI notation when prompted (e.g., "e2e4" to move a piece from e2 to e4).
5. The game continues until there's a checkmate, stalemate, or other game-ending condition.

## How It Works

- The game uses a standard starting position (FEN: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1").
- The Stockfish engine is set to analyze moves at a depth of 14.
- The current state of the board is displayed after each move.
- Invalid moves are rejected, and you'll be asked to input a valid move.

## Note

Make sure the path to the Stockfish executable in the script matches your actual Stockfish installation location:

```python
engine = chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-sse41-popcnt.exe")
```

Adjust this path if necessary for your system.

Enjoy your game of chess against the AI!