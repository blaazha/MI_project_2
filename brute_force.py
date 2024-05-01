import time
from entities import *
from itertools import combinations
from utils import sum_items_values
from output import items_to_csv
from statistics import describe_run

    
def brute_force(items):
    best_price = 0
    best_combination = None
    iter_log_bf = []
    counter = 0

    for r in range(1, len(items) + 1):
        for combination in combinations(items, r):
            total_price, total_weight = sum_items_values(combination)
            if total_price > best_price:
                best_combination = combination
                best_price = total_price
            counter += 1
            iter_log_bf.append((counter, best_price))
    return iter_log_bf, best_combination


