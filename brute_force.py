import time
from entities import *
from itertools import combinations
from utils import sum_items_values
from output import items_to_csv

NUM_OF_ITEMS = 15

items = [Item(i) for i in range(1, NUM_OF_ITEMS + 1)]
items_to_csv(items, file_name='brute_force_items.csv')

best_price = 0
best_combination = None
t0 = time.time()

for r in range(1, len(items) + 1):
    for combination in combinations(items, r):
        total_price, total_weight = sum_items_values(combination)
        if total_price > best_price:
            best_combination = combination
            best_price = total_price

t1 = time.time()
items_to_csv(items, file_name='brute_force_best_combination.csv')

print(f'Time spent: {t1 - t0}')
print(f'Used items: {len(best_combination)}')
print([item.__str__() for item in best_combination])
print(best_price)
