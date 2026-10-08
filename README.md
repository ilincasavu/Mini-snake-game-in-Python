# Snake

A classic Snake game built in Python with the built-in `turtle` module. Steer the snake around the board, eat food to grow, and avoid the walls and your own tail.

This is a beginner-friendly project that covers the basics of game development in Python: game loops, keyboard input, collision detection, and managing game state with lists.

## Features

- Smooth grid-based movement with arrow-key controls
- Snake grows each time it eats food
- Live score and high score display
- Collision detection for walls and the snake's own body
- Prevents instant 180-degree turns, so you can't reverse into yourself
- No external dependencies, just the Python standard library

## Requirements

- Python 3.8 or newer
- `tkinter` (used by `turtle`)

## Controls

| Key | Action     |
|-----|------------|
| ↑   | Move up    |
| ↓   | Move down  |
| ←   | Move left  |
| →   | Move right |

The snake starts moving as soon as you press the first arrow key.

## How it works

- **Head:** a single turtle that moves one grid square (20 px) per tick.
- **Body:** a list of turtle segments. Each tick, every segment moves to the position of the one in front of it (from back to front), and the first segment follows the head.
- **Game loop:** `game_loop()` checks for wall hits, food, and self-collision, then schedules itself again with `screen.ontimer`.
- **Scoring:** each piece of food is worth 10 points. The high score lasts until you close the game.

## Customization

Settings are at the top of `snake.py`:

| Setting    | Default | What it does                                  |
|------------|---------|-----------------------------------------------|
| `STEP`     | `20`    | Size of one grid square                       |
| `LIMIT`    | `280`   | How far from the center before hitting a wall |
| `DELAY_MS` | `100`   | Time between moves in ms (lower = faster)     |