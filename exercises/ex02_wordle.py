"""Wordle!"""

__author__ = "730710295"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def contains_char(wordle_word: str, guessed_letter: str) -> bool:
    """Returns True of False for a Single Guessed Character"""
    assert len(guessed_letter) == 1, f"len('{guessed_letter}') is not 1"
    i = 0
    while i < len(wordle_word):
        if guessed_letter == wordle_word[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Assigns an Emoji Which Colorcodes Guessed Words"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    statement: str = ""
    i = 0
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                statement += GREEN_BOX
            else:
                statement += YELLOW_BOX
        else:
            statement += WHITE_BOX
        i += 1
    return statement


def input_guess(expected_length: int) -> str:
    """Tells Player the Expected Length of Guessed Word"""
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    end_game: bool = False
    while turn < 7 and end_game == False:
        print(f"===Turn {turn}/6===")
        turn_number = input_guess(len(secret))
        print(emojified(turn_number, secret))
        if secret == turn_number:
            print(f"You won in {turn}/6 turns!")
            end_game = True
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
            end_game = True
        else:
            turn += 1


if __name__ == "__main__":
    main(secret="jinx")
