# Tic Tac Toe — Python Engine

A text-based Tic Tac Toe game built as a Python scripting exercise focused on logic design, state management, and clean game architecture.

This project emphasizes building a game engine first, then layering interaction on top of it.

---

## Project Goal

The goal is to implement a fully functional Tic Tac Toe engine using clean internal state representation and predictable game rules.

The focus is not GUI, but logic clarity and system structure.

---

## Engine Design

The board is represented internally as a 1D list with 9 positions:

```
[1,2,3,4,5,6,7,8,9]
```

This model simplifies indexing and win-condition checking while keeping the game state easy to manipulate.

The visual 3x3 board is derived from this internal representation.

---

## Game Architecture

The engine is built in modular steps:

1. Create the board (1D list state)
2. Display the board in readable format
3. Accept player input
4. Validate moves
5. Apply move to board
6. Check win conditions
7. Check draw condition
8. Switch player
9. Repeat game loop

Each step is implemented as a separate logical responsibility.

---

## Win Conditions

Winning combinations are defined as index patterns:

```
(0,1,2)
(3,4,5)
(6,7,8)
(0,3,6)
(1,4,7)
(2,5,8)
(0,4,8)
(2,4,6)
```

This allows clean and reusable win-check logic.

---

## Future Improvements

- Replay option
- Score tracking
- AI opponent
- GUI interface
- Web-based version
- Multiplayer over network

---

## Purpose

This project is part of a structured learning path focused on writing clear Python logic and building systems from scratch.

The emphasis is understanding how game rules map to data structures and control flow.
