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



class BagItem:

    def __init__(self, item: Item, is_included: bool):
        self.item = item
        self.is_included = is_included


class Statistics:
    def __init__(self, min, max, mean, median, std):
        self.min = min
        self.max = max
        self.mean = mean
        self.median = median
        self.std = std

    def __str__(self):
        return ("Statistics(min={}, max={}, mean={}, median={}, std={})"
                .format(self.min, self.max, self.mean, self.median, self.std))