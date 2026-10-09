import random
from stats import SessionStats
from words import WORDS, HINTS

DIFFICULTIES = {
    "easy": {"lives": 8, "base_score": 3},
    "medium": {"lives": 6, "base_score": 5},
    "hard": {"lives": 4, "base_score": 8},
}

class HangmanGame:
    def __init__(self):
        # Session-specific state (persists across all rounds)
        self.score = 0
        self.streak = 0
        self.stats = SessionStats()

        # Round-specific state
        self.category = "technology"
        self.difficulty = "medium"
        self.secret = ""
        self.guessed = set()
        self.wrong = set()
        self.lives = 6
        self.hint_used = False

    def choose_category(self):
        print("\nAvailable Categories:", ", ".join(WORDS.keys()))
        while True:
            cat = input("Choose category: ").strip().lower()
            if cat in WORDS:
                self.category = cat
                break
            print("Unknown category. Please choose from the list.")

    def choose_difficulty(self):
        print("\nAvailable Difficulties: easy, medium, hard")
        while True:
            diff = input("Choose difficulty [default: medium]: ").strip().lower()
            if not diff:
                self.difficulty = "medium"
                break
            if diff in DIFFICULTIES:
                self.difficulty = diff
                break
            print("Invalid choice. Please enter 'easy', 'medium', or 'hard'.")

    def start_round(self):
        # Reset round state
        self.choose_category()
        self.choose_difficulty()
        self.secret = random.choice(WORDS[self.category])
        self.guessed.clear()
        self.wrong.clear()
        self.lives = DIFFICULTIES[self.difficulty]["lives"]
        self.hint_used = False

    def get_masked_word(self):
        return " ".join([ch if ch in self.guessed else "_" for ch in self.secret])

    def use_hint(self):
        if self.hint_used:
            return None
        self.hint_used = True
        return HINTS.get(self.secret, "No hint available for this word.")

    def guess(self, letter):
        # Validate input format
        if len(letter) != 1 or not letter.isalpha():
            return "Enter one letter."

        # Task 1: Check both correct and wrong guesses so lives are not deducted repeatedly
        if letter in self.guessed or letter in self.wrong:
            return "Already guessed."

        if letter in self.secret:
            self.guessed.add(letter)
            return "Correct."
        else:
            self.wrong.add(letter)
            self.lives -= 1
            return "Wrong."

    def play_round(self):
        self.start_round()

        while self.lives > 0:
            print(f"\nWord: {self.get_masked_word()}")
            print(f"Lives: {self.lives} | Score: {self.score} | Streak: {self.streak}")
            print(f"Wrong guesses: {', '.join(sorted(self.wrong)) or 'None'}")

            raw = input("Guess a letter (or /hint, /quit): ").strip().lower()

            if raw == "/quit":
                return False

            if raw == "/hint":
                hint_text = self.use_hint()
                if hint_text:
                    print(f"Hint: {hint_text}")
                else:
                    print("Hint already used.")
                continue

            result = self.guess(raw)
            print(result)

            # Check win condition
            if all(ch in self.guessed for ch in self.secret):
                self.streak += 1
                base = DIFFICULTIES[self.difficulty]["base_score"]
                round_score = base + self.streak
                if self.hint_used:
                    round_score = max(0, round_score - 1)
                
                self.score += round_score
                self.stats.record(won=True, streak=self.streak)

                print(f"\nYou won! The word was '{self.secret}'.")
                print(f"Points earned this round: {round_score}")
                print(f"Current Score: {self.score} | Current Streak: {self.streak}")
                return True

        # Round loss condition
        self.streak = 0
        self.stats.record(won=False, streak=self.streak)
        print(f"\nGame Over! The word was '{self.secret}'.")
        print(f"Current Score: {self.score} | Streak reset to 0.")
        return True

    def display_session_stats(self):
        print("\n===============================")
        print("       SESSION SUMMARY         ")
        print("===============================")
        print(f"Total Rounds Played : {self.stats.rounds}")
        print(f"Total Rounds Won    : {self.stats.wins}")
        print(f"Best Streak Achieved: {self.stats.best_streak}")
        print(f"Final Score         : {self.score}")
        print("===============================")

    def run(self):
        print("=== Welcome to Hangman! ===")
        while True:
            keep_playing = self.play_round()
            if not keep_playing:
                break
            again = input("\nPlay another round? (y/n): ").strip().lower()
            if again != "y":
                break

        self.display_session_stats()