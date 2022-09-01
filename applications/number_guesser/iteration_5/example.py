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
        self.secret_number = randrange(1, max_number)
        self.attempts_allowed = attempts_allowed

    def run(self):
        for _ in range(self.attempts_allowed):  # we use "_" to declare a variable we are not going to use
            user_guess = self.get_user_guess()
            if user_guess == self.secret_number:
                success()
                break
            else:
                fail()
        game_over()

    def get_user_guess(self) -> int:
        try:
            user_guess = int(input("Your guess \n"))
            return user_guess
        except ValueError:
            wrong_input()
            return self.get_user_guess()


if __name__ == "__main__":
    game = GuessGame(11, attempts_allowed=3)
    game.run()
