import random
import math
from entities import Item, BagItem
from utils import sum_bag_items_values
import copy


def simulated_annealing(items: [Item]):
    # PARAMS
    T0 = 12
    T_decrease = 0.011999
    metropolis_calls = 10
    iterations = 1000
    #
    T = T0
    current_state = [BagItem(item, random.randint(0, 5) < 3) for item in items]
    fitness_arr = []

    for i in range(iterations):
        for j in range(metropolis_calls):
            new_state = __sa_generate_new_state(current_state=current_state, T=T)
            if __sa_accept_solution(sum_bag_items_values(current_state), sum_bag_items_values(new_state), T):
                current_state = new_state
            fitness_arr.append((i * metropolis_calls + j + 1, sum_bag_items_values(current_state)))
        T -= T_decrease

    return fitness_arr, current_state


def __sa_accept_solution(current_score, next_score, T) -> bool:
    if current_score < next_score:
        return True
    if next_score == 0:
        return False
    threshold = 1 - pow(math.e, -(next_score - current_score)/T)
    rnd = random.uniform(0, 1)
    return rnd <= threshold


def __sa_generate_new_state(current_state, T):
    new_state = copy.deepcopy(current_state)
    flip_probability = min(0.5, T / (2 * 12))
    for item in new_state:
        if random.random() < flip_probability:
            item.is_included = not item.is_included
    return current_state
