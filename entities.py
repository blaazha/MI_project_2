import random


class Item:
    id: int
    price: int
    weight: int

    def __init__(self, id):
        self.id = id
        self.price = random.randint(1, 51)
        self.weight = random.randint(1, 51)

    def __str__(self):
        return f'ID: {self.id} Price: {self.price}  Weight: {self.weight}'
