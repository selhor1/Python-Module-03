import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = dict()

    for arg in sys.argv[1:]:
        parts = arg.split(":")
        name = parts[0]
        qty = int(parts[1])
        inventory.update({name: qty})

    total_items = 0
    for v in inventory.values():
        total_items += v

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    for item, qty in sorted(inventory.items(), key=lambda x: -x[1]):
        percent = (qty / total_items) * 100
        print(f"{item}: {qty} units ({percent:.1f}%)")

    if len(inventory) == 0:
        print("No items to analyze.")
        print("=== Inventory Statistics ===")
        print("Most abundant: None")
        print("Least abundant: None")
        sys.exit()

    print("\n=== Inventory Statistics ===")

    most_item = None
    least_item = None

    for item, qty in inventory.items():
        if most_item is None or qty > inventory.get(most_item):
            most_item = item
        if least_item is None or qty < inventory.get(least_item):
            least_item = item

    print(f"Most abundant: {most_item} ({inventory.get(most_item)} units)")
    print(f"Least abundant: {least_item} ({inventory.get(least_item)} "
          f"unit{'s' if inventory.get(least_item) > 1 else ''})")

    print("\n=== Item Categories ===")

    moderate = dict()
    scarce = dict()

    for item, qty in inventory.items():
        if qty >= 5:
            moderate.update({item: qty})
        else:
            scarce.update({item: qty})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")

    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)

    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")

    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
