from entities import Item
import numpy as np
import random
from utils import __max_capacity, average_score
import matplotlib.pyplot as plt
from statistics import describe_run
from brute_force import brute_force
from output import items_to_csv
import time

def simulated_annealing(items, capacity, temp, cooling_rate, steps, swap_prob=0.1):
    n = len(items)
    current_solution = np.zeros(n, dtype=int)
    current_value = 0
    current_weight = 0

    # Initialize with a random solution within the capacity
    while current_weight == 0:  # Ensure at least one item is selected
        for i in range(n):
            if np.random.rand() < 0.5:
                item = items[i]
                if current_weight + item.weight <= capacity:
                    current_solution[i] = 1
                    current_value += item.price
                    current_weight += item.weight

    best_solution = current_solution.copy()
    best_value = current_value

    iteration_log = []  # To store the iteration number and best value found

    total_iterations = 0  # Track the total number of iterations

    for i in range(steps):
        for _ in range(10):
            new_solution = current_solution.copy()
            new_value = current_value
            new_weight = current_weight

            for i in range(n):
                if np.random.rand() < swap_prob:
                    new_solution[i] = 1 - new_solution[i]
                    item = items[i]
                    if new_solution[i] == 1:  # Item is added
                        new_weight += item.weight
                        new_value += item.price
                    else:  # Item is removed
                        new_weight -= item.weight
                        new_value -= item.price

            # Check if the new solution is feasible
            if new_weight <= capacity:
                # Accept new solution if it's better or based on acceptance probability
                if new_value > current_value or np.random.rand() < np.exp((new_value - current_value) / temp):
                    current_solution = new_solution.copy()
                    current_value = new_value
                    current_weight = new_weight

                    # Update the best solution found
                    if new_value > best_value:
                        best_solution = new_solution.copy()
                        best_value = new_value

            iteration_log.append((total_iterations, best_value))  # Log the iteration and value
            total_iterations += 1  # Increment total iteration count

        temp -= cooling_rate  # Cool down

    return best_solution, best_value, [items[i] for i in range(n) if best_solution[i] == 1], iteration_log

# Generating items
num_items = 15
items = [Item(i) for i in range(num_items)]
items_to_csv(items, "items.csv")

# Knapsack parameters
capacity = __max_capacity(len(items))
initial_temp = 12
cooling_rate = 0.011999
steps = 1000
swap_probability = 0.1  # Probability to swap inclusion of an item

# Solve the problem
iter_logs = []
for i in range(30):
    t0 = time.time()
    solution, max_value, selected_items, iteration_log = simulated_annealing(items, capacity, initial_temp, cooling_rate, steps, swap_probability)
    t1 = time.time()
    print(f'Time spent (SA): {t1 - t0}')
    iter_logs.append(iteration_log)
    #print(solution, max_value, [i.__str__() for i in selected_items])

# Plotting the results
avg_out = average_score(iter_logs)
iterations, values = [a[0] for a in avg_out],  [a[1] for a in avg_out]
plt.plot(iterations, values, marker='', label='Simulované žíhání')
plt.xlabel('Iteration Number')
plt.ylabel('Best Value Found')
plt.title('Průměrné výsledky sanazených algoritmů')


print(describe_run(iter_logs))


#### BF (tohle by stacilo zapnout jen jednou ...)


logs_bf = []
best_combination = None
for i in range(30):
    t0 = time.time()
    l, combination = brute_force(items)
    logs_bf.append(l)
    t1 = time.time()
    print(f'Time spent (brute force): {t1 - t0}')
    best_combination = combination
print(describe_run(logs_bf))

items_to_csv(best_combination, 'best_combination.csv')
avg_out_bf = average_score(logs_bf)
iterations_bf, values_bf = [a[0] for a in avg_out_bf],  [a[1] for a in avg_out_bf]
plt.plot(iterations_bf, values_bf, marker='', label='Brute force')
plt.legend()
plt.savefig('outputs/avg_out.png')
plt.show()