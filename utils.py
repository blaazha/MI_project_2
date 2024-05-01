from entities import Item, BagItem


def __max_capacity(items_count: int) -> int:
    if items_count <= 15:
        return 100
    elif items_count <= 30:
        return 200
    return 300


def sum_items_values(items: list[Item]):
    total_weight = sum([item.weight for item in items])
    total_price = 0
    if total_weight <= __max_capacity(len(items)):
         total_price = sum([item.price for item in items])
    return total_price, total_weight


def sum_bag_items_values(bagitems: list[BagItem]):
    total_price, total_weight = sum_items_values([bagitem.item for bagitem in bagitems if bagitem.is_included])
    return total_price if total_weight <= __max_capacity(len(bagitems)) else 0


def average_score(steps):
    num_of_steps = len(steps[0])
    avg_steps = []
    for i in range(num_of_steps):
        step_avg = 0.0
        for j in range(len(steps)):
            step_avg += steps[j][i][1]
        avg_steps.append((i, step_avg / len(steps)))
    return avg_steps