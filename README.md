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

# FP-Project2-2025
FP Scrabble Project — TADs Extension - IST LEIC 2024/2025

A Python implementation of Scrabble redesigned around Abstract Data Types (TADs), developed as Project 2 for Fundamentos de Programação (Foundations of Programming) at Instituto Superior Técnico, LEIC 2024/2025. Builds on Project 1, restructuring the game around explicit abstraction barriers between each type's internal representation and its public interface.

The project implements the following TADs from scratch in Python, including:

Square (`casa`) TAD — board position (row, column), with constructor, selectors, recognizer, equality test, transformers (`casa_para_str` / `str_para_casa`), and a high-level function to increment a position in a given direction (`incrementa_casa`)
Player (`jogador`) TAD — supports both human players (with a name) and computer agents (with a difficulty level: FACIL, MEDIO, DIFICIL), sharing common operations (points, letters) through type-aware recognizers
Vocabulary (`vocabulario`) TAD — validates the set of words allowed in the game, ensuring each word uses only valid letters and respects length limits

Key concepts demonstrated
Abstract Data Type design with clear abstraction barriers (constructors, selectors, modifiers, recognizers, tests, transformers)
Simple polymorphism via dictionaries with a `'tipo'` field (human vs. agent)
Separation between internal data representation and the public interface used by the rest of the program

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


License

MIT
