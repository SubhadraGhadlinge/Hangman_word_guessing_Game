# Hangman Word Guessing Game 

A console-based Hangman game developed using Python 3. The player guesses a hidden English word one letter at a time, with a maximum of six incorrect guesses.

## Project Overview

•	Python 3

•	Python Standard Library ("random", "pathlib")

•	Visual Studio Code


The Hangman Word Guessing Game is a beginner-friendly Python project that demonstrates string manipulation, loops, conditional statements, functions, file handling, and random word selection.

## Features

•	Random selection of a secret word from a text file

•	Interactive console-based gameplay

•	ASCII art gallows updated after incorrect guesses

•	Maximum of six incorrect guesses

•	Tracks previously guessed letters

•	Prevents duplicate guesses from deducting attempts

•	Validates user input and displays error messages

•	Displays victory or defeat messages

•	Option to play again



## Technologies Used

•	Python 3

•	Python Standard Library ("random", "pathlib")

•	Visual Studio Code


## Project Structure
``` 
hangman-word-guessing-game/

├── hangman.py
├── hangman_word_guessing_game_data.txt
├── README.md
```

## Requirements

Python 3 installed on your computer
A code editor such as Visual Studio Code
The English word-list text file included in this repository

## How to Run

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project folder.
4. Run the following command:

```cmd
python hangman.py
```

On Windows, you can also use:
```cmd
py hangman.py
```

5. Follow the on-screen instructions and enter one letter at a time.

## How to Play

1. The game selects a random word.
2. The hidden word is displayed using underscores.
3. Enter one alphabetic letter at a time.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses update the ASCII gallows and reduce the remaining attempts.
6. Guess the complete word before running out of attempts to win.

## Concepts Learned

•	Python functions and modular programming   

•	Loops and conditional statements

•	String manipulation

•	Lists and sets

•	File handling

•	Random selection

•	Input validation

•	Exception and error handling

## Sample Output 
```
============================================
       HANGMAN WORD GUESSING GAME
============================================

Guess the hidden word, one letter at a time.
You have 6 incorrect guesses available.

     +---+
     |   |
         |
         |
         |
         |
    =========

Word:              _ _ _ _ _ _
Guessed letters:   None
Attempts left:     6

Guess a letter: a
Sorry, 'a' is not in the word.

     +---+
     |   |
     O   |
         |
         |
         |
    =========

Word:              _ _ _ _ _ _
Guessed letters:   a
Attempts left:     5

Guess a letter: 7
Please enter a single letter (A-Z).

Guess a letter: a
You already guessed 'a'. No attempt is deducted.

Guess a letter: e
Good guess! 'e' is in the word.

Word:              _ e _ _ _ _
Guessed letters:   a e
Attempts left:     5

============================================
             GAME OVER
============================================
The word was: python
Better luck next time!
```
## Author
Created as a beginner Python programming project to practice programming fundamentals and problem-solving.

