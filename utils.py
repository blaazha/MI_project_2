from entities import Item


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
