# Tic-Tac-Toe with Pygame

A two-player, local Tic-Tac-Toe game built in Python using Pygame. Players take turns clicking a 3×3 grid to place Xs and Os. The game detects winning rows, columns, and diagonals.

## Features

* Local two-player gameplay (X goes first)
* Mouse-controlled 3×3 board
* Prevents moves in occupied squares
* Automatically alternates between X and O
* Detects horizontal, vertical, and diagonal wins
* Stops accepting moves after a win

## Getting Started

### Requirements

* Python 3
* Pygame

### Installation and Running

1. Download or clone this repository.

2. Open a terminal in the project folder.

3. Install Pygame:

   ```bash
   python -m pip install pygame
   ```

4. Start the game (assuming the file is named `tic_tac_toe.py`):

   ```bash
   python tic_tac_toe.py
   ```

Depending on your system, you may need to use `python3` instead of `python`.

## How to Play

1. Run the program to open the game window.
2. Player **X** clicks an empty square to make the first move.
3. Player **O** clicks an empty square next; players continue alternating.
4. The first player to occupy three squares in a row, column, or diagonal wins.
5. The winning message is printed **in the terminal**, not inside the game window. Close the game window to exit.

## How It Works

**Game State**

The `clicked_boxes` list stores each move as a tuple containing the row, column, and player.

**Move Validation**

The `box_checker()` function determines whether a square has already been selected, preventing players from overwriting existing moves.

**Rendering**

Pygame draws the board and displays Xs and Os using lines and circles.

**Turn Management**

The `current_player` variable tracks whose turn it is and switches between players after each valid move.

**Win Detection**

The game evaluates all eight possible winning combinations, including horizontal, vertical, and diagonal lines.

## Project Structure

```text
tic-tac-toe-pygame/
├── tic_tac_toe.py    # Python source code
└── README.md         # Project documentation
```

## Current Limitations and Potential Improvements

Future improvements could include:

* Displaying the winner directly in the game window.
* Detecting and announcing draws.
* Adding a restart button.
* Tracking player scores across multiple games.
* Simplifying repetitive drawing and win-condition logic using loops and reusable data structures.

## What I Learned

Building this project gave me practical experience with:

* Python functions, loops, and conditional statements.
* Managing game state using lists and tuples.
* Processing mouse events and user input.
* Working with 2D coordinates.
* Drawing graphical elements with Pygame.
* Implementing game rules and win-condition logic.

## Authorship and AI Disclosure

**The Tic-Tac-Toe game code was written by me. This README documentation was written with the assistance of AI (ChatGPT), based on my original source code.**
