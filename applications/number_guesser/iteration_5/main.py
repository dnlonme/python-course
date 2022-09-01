from random import randrange


def success():
    print("You nailed it!")


def fail():
    print("You're a loser!")


def game_over():
    print("Game Over!")


def wrong_input():
    print("Pleases enter a number!")


class GuessGame:
    def __init__(self, max_number: int, attempts_allowed: int):
        pass


if __name__ == "__main__":
    game = GuessGame(11, attempts_allowed=3)
    game.run()
