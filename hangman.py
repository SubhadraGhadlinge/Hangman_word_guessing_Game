import random
from pathlib import Path

MAX_ATTEMPTS = 6
WORD_FILE = Path(__file__).with_name("hangman_word_guessing_game_data.txt")

HANGMAN_STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
]

FALLBACK_WORDS = [
    "python", "computer", "programming", "keyboard", "student",
    "science", "database", "internet", "software", "developer",
    "algorithm", "function", "variable", "network", "college",
]


def load_words():
    # Load usable alphabetic words from the supplied words.txt file.
    try:
        with WORD_FILE.open("r", encoding="utf-8", errors="ignore") as file:
            words = {
                line.strip().lower()
                for line in file
                if line.strip().isalpha() and len(line.strip()) >= 4
            }
        if words:
            return sorted(words)
        print("Warning: words.txt has no suitable words; using built-in words.")
    except OSError:
        print("Warning: words.txt was not found; using built-in words.")
    return FALLBACK_WORDS


def display_game(secret_word, guessed_letters, wrong_guesses):
    #Display the current gallows, masked word, and guessed letters.
    print(HANGMAN_STAGES[len(wrong_guesses)])
    masked_word = " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )
    print("\nWord:             ", masked_word)
    print("Incorrect guesses:", " ".join(sorted(wrong_guesses)) or "None")
    print("Guessed letters:  ", " ".join(sorted(guessed_letters)) or "None")
    print(f"Attempts left:     {MAX_ATTEMPTS - len(wrong_guesses)}")


def play_round(words):
    # Run one round. Return True if the player wins, otherwise False.
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()

    print("\nGuess the hidden word, one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses available.")

    while len(wrong_guesses) < MAX_ATTEMPTS:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word.upper())
            return True

        guess = input("\nEnter one letter (or type 'quit' to stop): ").strip().lower()

        if guess == "quit":
            print(f"\nGame stopped. The word was: {secret_word.upper()}")
            return False

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. No attempt is deducted.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses.add(guess)
            print(f"Incorrect! '{guess}' is not in the word.")

    display_game(secret_word, guessed_letters, wrong_guesses)
    print("\nGame over! You used all 6 incorrect guesses.")
    print("The correct word was:", secret_word.upper())
    return False


def main():
    # Main menu and replay control.
    words = load_words()
    print("=" * 44)
    print("       HANGMAN WORD GUESSING GAME")
    print("=" * 44)
    print(f"Word list loaded: {len(words)} words")
    wins = 0
    rounds = 0

    while True:
        won = play_round(words)
        rounds += 1
        if won:
            wins += 1

        print(f"\nScore: {wins} win(s) out of {rounds} round(s).")
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("\nThanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame closed. Thanks for playing!")
