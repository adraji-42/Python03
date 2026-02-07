def create_item(
    name: str, category: str, rarity: str, quantity: int, price: int
) -> dict:
    """
    Helper function to create an item structure.

    Args:
        name: The display name of the item.
        category: The type of item (e.g., weapon, armor).
        rarity: How rare the item is.
        quantity: The number of items.
        price: The cost of a single unit in gold.

    Returns:
        A dictionary containing the item properties.
    """

    if quantity < 0:
        print("Warning: The quantity cannot be negative. "
              "The value will be zeroed out.")
        quantity = 0

    if price < 0:
        print("Warning: The price cannot be negative. "
              "The value will be zeroed out.")
        price = 0

    return {
        "name": name,
        "category": category,
        "rarity": rarity,
        "quantity": quantity,
        "price": price
    }


def display_inventory(name: str, inventory: dict[str, dict]) -> None:
    """
    Prints a detailed report of a player's inventory.

    Args:
        name: The name of the player.
        inventory: The dictionary containing all player items.
    """
    print(f"=== {name}'s Inventory ===")
    total_price = 0
    total_items = 0
    categories: dict[str, int] = {}

    if not inventory:
        print(f"{name}'s inventory is empty!\n")
        return

    for item in inventory.values():
        subtotal = item['quantity'] * item['price']
        total_price += subtotal
        total_items += item['quantity']

        cat = item['category']
        categories[cat] = categories.get(cat, 0) + item['quantity']

        print(f"{item['name']} ({item['category']}, {item['rarity']}): "
              f"{item['quantity']}x @ {item['price']} gold each = "
              f"{subtotal} gold")

    cat_list = [f"{c}({q})" for c, q in categories.items()]
    print(f"\nInventory value: {total_price} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: {', '.join(cat_list)}\n")


def transaction(
    p1: tuple[str, dict[str, dict]],
    p2: tuple[str, dict[str, dict]],
    item_name: str,
    quantity: int
) -> None:
    """
    Handles item transfer between two players.

    Args:
        p1: Tuple containing (name, inventory) of the sender.
        p2: Tuple containing (name, inventory) of the receiver.
        item_name: The name of the item to transfer.
        quantity: The amount to transfer.
    """
    name1, inv1 = p1
    name2, inv2 = p2

    print(
        f"=== Transaction: {name1} gives {name2} {quantity} {item_name}s ==="
    )

    if item_name not in inv1:
        print(f"Transaction failed! {name1} does not have: {item_name}\n")
        return

    if inv1[item_name]['quantity'] < quantity:
        print(f"Transaction failed! Not enough {item_name}\n")
        return

    inv1[item_name]['quantity'] -= quantity

    if item_name in inv2:
        inv2[item_name]['quantity'] += quantity
    else:
        ref = inv1[item_name]
        inv2[item_name] = create_item(
            item_name, ref['category'], ref['rarity'], quantity, ref['price']
        )

    print("Transaction successful!")
    print(f"Updated {item_name} - {name1}: {inv1[item_name]['quantity']}, "
          f"{name2}: {inv2[item_name]['quantity']}\n")


def run_analytics(players: dict[str, dict]) -> None:
    """
    Generates analytics about all players' inventories.

    Args:
        players: Dictionary containing all player names and their inventories.
    """
    print("=== Inventory Analytics ===")
    most_valuable_player = ""
    max_value = -1
    most_items_player = ""
    max_items = -1
    rare_items: list[str] = []

    for name, inv in players.items():
        current_value = sum(i['price'] * i['quantity'] for i in inv.values())
        current_items = sum(i['quantity'] for i in inv.values())

        if current_value > max_value:
            max_value = current_value
            most_valuable_player = name
        if current_items > max_items:
            max_items = current_items
            most_items_player = name

        for item in inv.values():
            if item['rarity'] not in ["common", "uncommon"]:
                if item['name'] not in rare_items:
                    rare_items.append(item['name'])

    print(f"Most valuable player: {most_valuable_player} ({max_value} gold)")
    print(f"Most items: {most_items_player} ({max_items} items)")
    print(f"Rarest items: {', '.join(rare_items)}\n")


def main() -> None:
    """Initialize player data and run the inventory system."""
    players = {
        "Yasuo": {
            "Blade of the Ruined King": create_item(
                "Blade of the Ruined King", "weapon", "epic", 1, 3200
            ),
            "Infinity Edge": create_item(
                "Infinity Edge", "weapon", "epic", 1, 3500
            ),
            "Refillable Potion": create_item(
                "Refillable Potion", "consumable", "common", 2, 150
            ),
            "Berserker's Greaves": create_item(
                "Berserker's Greaves", "armor", "uncommon", 1, 1100
            )
        },
        "Zac": {
            "Sunfire Aegis": create_item(
                "Sunfire Aegis", "armor", "rare", 1, 2700
            ),
            "Mercury's Treads": create_item(
                "Mercury's Treads", "armor", "uncommon", 1, 1250
            )
        }
    }

    print("=== Player Inventory System ===\n")
    try:
        display_inventory("Yasuo", players['Yasuo'])
    except Exception as e:
        print(f"Unexpected error while displaying inventory. {e}")

    try:
        transaction(
            ("Yasuo", players['Yasuo']),
            ("Zac", players['Zac']),
            "Refillable Potion", 1
        )
    except Exception as e:
        print(f"Unexpected error while processing transaction. {e}")

    try:
        run_analytics(players)
    except Exception as e:
        print(f"Unexpected error while analyzing. {e}")


if __name__ == "__main__":
    main()
