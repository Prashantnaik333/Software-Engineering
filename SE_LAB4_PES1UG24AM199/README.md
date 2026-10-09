# Scenario 16 — Hangman Challenge

A multi-round, terminal-based Hangman game built with Python. Players guess a hidden word from a selected category, use an optional hint, choose a difficulty level, and track their score and streak across rounds.

## Features

- **Word categories:** Technology, Science, and Culture.
- **Difficulty levels:**
  - Easy — 8 lives, base score of 3 points.
  - Medium — 6 lives, base score of 5 points.
  - Hard — 4 lives, base score of 8 points.
- **Guess validation:** Rejects malformed input and prevents a previously guessed correct or incorrect letter from being counted again.
- **Hints:** One hint per round.
- **Scoring:** Winning earns the selected difficulty's base score plus the updated win streak; using a hint reduces that round's reward by 1 point, with a minimum reward of 0.
- **Session statistics:** Tracks rounds played, rounds won, and best streak in memory.
- **Multiple rounds:** Round state resets between rounds while the session score and statistics remain available.
- **Quit command:** Enter `/quit` during a round to stop playing.

## Requirements

- Python 3.9 or newer is recommended.
- Uses only the Python standard library; no third-party packages are required.

## Project structure

```text
scenario-04-hangman/
├── README.md
├── main.py
├── game.py
├── words.py
├── stats.py
└── requirements.txt
```

## Setup and run

1. Install Python 3.9 or newer.
2. Place all project files in the same directory.
3. Open a terminal in that directory.
4. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## How to play

1. Start the game.
2. Choose a category: `technology`, `science`, or `culture`.
3. Choose a difficulty: `easy`, `medium`, or `hard`. Press Enter to use Medium.
4. Enter one letter at a time to guess the hidden word.
5. Enter `/hint` to reveal the word's hint. A hint can be used once per round.
6. Enter `/quit` to leave the current game loop.
7. After a round, choose `y` to play another round or any other response to finish and view the session summary.

## Scoring and lives

| Difficulty | Starting lives | Base score |
|---|---:|---:|
| Easy | 8 | 3 |
| Medium | 6 | 5 |
| Hard | 4 | 8 |

When a player wins, the round reward is calculated as:

```text
round score = difficulty base score + current win streak
```

If a hint was used, 1 point is deducted from that round's reward, but the reward cannot go below zero. The session score accumulates rewards from won rounds. Losing resets the current streak to zero.

## Project files

- **`main.py`** — Application entry point; creates `HangmanGame` and starts the game.
- **`game.py`** — Contains the game loop, category and difficulty selection, round state, input validation, guessing, hints, scoring, and session summary.
- **`words.py`** — Holds the word lists and corresponding hints for each category.
- **`stats.py`** — Implements `SessionStats`, which records rounds played, wins, and best streak.
- **`requirements.txt`** — Documents that the project uses only Python's standard library.

## Important behaviour

- A valid new correct guess reveals matching letters and does not cost a life.
- A valid new incorrect guess costs one life.
- Repeating either a correct or incorrect guess displays `Already guessed.` and does not change lives or other game state.
- Invalid guesses, such as `ab`, `7`, or `@`, display an error and do not count as guesses.
- The game keeps session score and statistics in memory only. No database or persistent storage is used.

## Testing checklist

Use this checklist before submission:

- [ ] Repeat a wrong guess and confirm that lives decrease only once for that letter.
- [ ] Repeat a correct guess and confirm it is not counted twice.
- [ ] Enter invalid inputs such as `ab`, `7`, and `@`; verify the game state does not change.
- [ ] Use `/hint` once, then try it again and confirm the second attempt is rejected.
- [ ] Test all three categories.
- [ ] Test Easy, Medium, and Hard and verify the starting lives and scoring.
- [ ] Win a round and confirm the score and streak update.
- [ ] Lose a round and confirm the streak resets.
- [ ] Play multiple rounds and confirm session statistics accumulate.
- [ ] Enter `/quit` and verify the game exits the round loop.

## Lab 4 submission checklist

According to the lab handout, prepare these three items:

- [ ] A 10-second video showing the original bug before the fix.
- [ ] A 10-second video showing the fixed bug and new features after the fix.
- [ ] A link to the complete LLM/chat history used during the lab.

The lab also asks you to reproduce the original defect before fixing it, test the required edge cases, keep the implementation modular, avoid unnecessary dependencies and persistent storage, and maintain separate commits for the tasks.

## Known implementation note

The current `game.py` calls `choose_category()` and `choose_difficulty()` at the start of every round. This means players are prompted to choose them again for each new round. If that is intentional, no change is needed; otherwise, move selection outside the per-round setup.

## License

No license information is specified in the provided project files.
