from sys import argv, exit


def argv_parsing() -> dict[str, int]:

    items: dict[str, int] = {}
    input_items = argv[1:]

    if len(input_items) == 0:
        print("No items provided.\n\tUsage: python3 ft_inventory_system.py "
              "<item1:quantity> <item2:quantity> ...\n")
        exit(1)

    for item in input_items:
        if item.count(':') != 1:
            raise ValueError(f"Invalid item input form from arg: '{item}'.")

        name, quantity_str = item.capitalize().split(':')

        try:
            quantity = int(quantity_str)
            items[name] = items.get(name, 0) + quantity
        except ValueError:
            raise ValueError(f"Quantity for '{name}' must be an integer.")

    return items


def inventory_analysis(inventory: dict[str, int]) -> None:

    if not inventory:
        print("Empty inventory")
        return

    print("=== Inventory System Analysis ===")
    total_items = sum(inventory.values())
    unique_items = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    print("\n=== Current Inventory ===")

    max_qty = -1
    min_qty = total_items + 1
    most_items = []
    least_items = []

    for n, q in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
        print(f"{n}: {q} units ({(q / total_items * 100):.1f}%)")

        if q > max_qty:
            max_qty = q
            most_items = [n]
        elif q == max_qty:
            most_items.append(n)

        if q < min_qty:
            min_qty = q
            least_items = [n]
        elif q == min_qty:
            least_items.append(n)

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {', '.join(most_items)} ({max_qty} units)")
    print(f"Least abundant: {', '.join(least_items)} ({min_qty} units)")

    print("\n=== Item Categories ===")
    scarce = {n: q for n, q in inventory.items() if n not in most_items}
    moderate = {n: q for n, q in inventory.items() if n in most_items}

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    needed = [item for item in scarce if scarce[item] == min(scarce.values())]
    print(f"Restock needed: {needed}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'Sword' in inventory: {'Sword' in inventory}")


def main() -> None:

    try:
        items = argv_parsing()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        inventory_analysis(items)


if __name__ == "__main__":
    main()
