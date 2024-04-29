import csv
from entities import Item

OUTPUT_FOLDER = './outputs/'


def items_to_csv(items: [Item], file_name: str = 'items.csv'):
    with open(OUTPUT_FOLDER + file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['ID', 'Price', 'Weight'])
        # Write the item data
        for item in items:
            writer.writerow([item.id, item.price, item.weight])

