import random
from dataclasses import dataclass
from typing import List


# Remember this boy? Think about which method can become classmethod
class GuessGame:
    def __init__(self, max_number: int, attempts_allowed: int):
        self.secret_number = random.randrange(1, max_number)
        self.attempts_allowed = attempts_allowed

    def run(self):
        for _ in range(self.attempts_allowed):  # we use "_" to declare a variable we are not going to use
            user_guess = self.get_user_guess()
            if user_guess == self.secret_number:
                print("YEEEEEEEEEAH")
                return
            else:
                print("NOOOOOO")
        print("GameOver")

    def get_user_guess(self) -> int:
        try:
            user_guess = int(input("Your guess \n"))
            return user_guess
        except ValueError:
            print("FK U")
            self.get_user_guess()


@dataclass
class OrderItem:
    name: str
    price: int
    amount: int

    @property
    def sum(self) -> int:
        """Should calculate order item sum"""
        pass


@dataclass
class Order:
    items: List[OrderItem]

    # And may be some other attributes, like user, date, status etc
    @property
    def sum(self) -> int:
        """Should return order sum"""
        pass

    def add_item(self, item: OrderItem) -> None:
        """Should add order item to order"""
        pass


apple_item = OrderItem(name="apple", price=10, amount=2)
tomato_item = OrderItem(name="tomate", price=20, amount=5)

order = Order(items=[])
order.add_item(apple_item)
assert order.sum == 20, "Wrong"
order.add_item(tomato_item)
assert order.sum == 120, "Wrong"

print("Done")
