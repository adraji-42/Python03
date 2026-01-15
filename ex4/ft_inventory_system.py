def create_item(
    name: str, category: str, rarity: str, quantity: int, price: int
):
    """Helper function to create an item structure."""
    return {
        "name": name,
        "category": category,
        "rarity": rarity,
        "quantity": quantity,
        "price": price
    }


def display_inventory(name: str, inventory: dict):
    """Prints a detailed report of a player's inventory."""

    print(f"=== {name}'s Inventory ===")
    total_price = 0
    total_items = 0
    categories = {}

    if len(inventory) < 1:
        print(f"{name}'s inventory is empty!")
        return

    for item in inventory.values():
        total_price += item["quantity"] * item["price"]
        total_items += item["quantity"]

        cat = item["category"]
        categories[cat] = categories.get(cat, 0) + item["quantity"]

        print(f"{item['name']} ({item['category']}, {item['rarity']}): "
              f"{item['quantity']}x @ {item['price']} gold each = "
              f"{item['quantity'] * item['price']} gold")
    print("")

    cat_list = [f"{c}({q})" for c, q in categories.items()]
    print(f"Inventory value: {total_price} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: {', '.join(cat_list)}\n")


def transaction(p1: tuple, p2: tuple, item: str, qty: int):
    """Handles item transfer between two players."""

    name1, inv1 = p1
    name2, inv2 = p2

    print(f"=== Transaction: {name1} gives {name2} {qty} {item}s ===")

    if item not in inv1 or len(inv1) < 1:
        print(f"Transaction failed! {name1} is not have this item: {item}")
        return
    if inv1[item]["quantity"] < qty:
        print("Transaction failed!"
              f"{name1} does not have enough of this item: {item}")

    # Deduct from player 1
    inv1[item]["quantity"] -= qty

    # Add to player 2
    if item in inv2:
        inv2[item]["quantity"] += qty
    else:
        # Create a new item for p2 based on p1's item data
        ref = inv1[item]
        inv2[item] = create_item(
            item, ref["category"], ref["rarity"], qty, ref["price"]
        )

    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"{name1} potions: {inv1['potion']['quantity']}")
    print(f"{name2} potions: {inv2['potion']['quantity']}\n")


def run_analytics(players: dict):
    """Generates analytics about all players' inventories."""

    print("=== Inventory Analytics ===")
    most_valuable_player = ""
    max_value = -1
    most_items_player = ""
    max_items = -1
    all_rarities = {}

    for name, inv in players.items():
        current_value = sum(i["price"] * i["quantity"] for i in inv.values())
        current_items = sum(i["quantity"] for i in inv.values())

        if current_value > max_value:
            max_value = current_value
            most_valuable_player = name
        if current_items > max_items:
            max_items = current_items
            most_items_player = name

        for item in inv.values():
            if item["rarity"] not in ["common", "uncommon"]:
                all_rarities[item["name"]] = True

    print(f"Most valuable player: {most_valuable_player} ({max_value} gold)")
    print(f"Most items: {most_items_player} ({max_items} items)")
    print(f"Rarest items: {', '.join(all_rarities.keys())}")


def main():

    players = {
        "Yasuo": {
            "sword": create_item("sword", "weapon", "rare", 1, 500),
            "potion": create_item("potion", "consumable", "common", 5, 50),
            "shield": create_item("shield", "armor", "uncommon", 1, 200)
        },
        "Zac": {
            "magic_ring": create_item(
                    "magic_ring", "artifact", "epic", 1, 1000
                )
        }
    }

    print("=== Player Inventory System ===\n")
    display_inventory("Yasuo", players["Yasuo"])

    list_players = [(p, i) for p, i in players.items()]
    transaction(
        list_players[0],
        list_players[1],
        "potion", 2
    )

    run_analytics(players)


if __name__ == "__main__":
    main()
