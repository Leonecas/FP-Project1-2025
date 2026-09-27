# FP-Project1-2025
FP Scrabble Project - IST LEIC 2024/2025

A command-line implementation of Scrabble, developed as Project 1 for Fundamentos de Programação (Foundations of Programming) at Instituto Superior Técnico, LEIC 2024/2025.

The project implements the full game logic from scratch in Python, including:

Letter set/bag creation and a custom xorshift-based pseudo-random number generator for shuffling
Board creation and manipulation (inserting/querying letters, extracting sequences, placing words)
Player creation, letter distribution, and score tracking
Full turn-based gameplay: playing words, exchanging letters, passing, and validating moves against Scrabble rules (first move through the center square, word adjacency to existing tiles, letter availability)
Key concepts demonstrated
Custom pseudo-random number generation (xorshift algorithm) — no external random library used
Dictionary-based data modeling for letter sets and player state
Coordinate-based 2D board representation and directional (horizontal/vertical) string extraction
Input validation and defensive programming (raising errors on invalid arguments)
How to run
```bash
python scrabble.py
```

You'll be prompted for each player's move in the format:

J <row> <col> <H|V> <word> — play a word
T <letters> — exchange letters
P — pass your turn


License

MIT
