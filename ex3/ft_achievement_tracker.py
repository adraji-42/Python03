def main():
    print("=== Achievement Tracker System ===", end="\n\n")

    players_data = {
        "Chaos": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "rida2015": {"first_kill", "level_10", "boss_slayer", "collector"},
        "Spacha": {
            "level_10", "treasure_hunter",
            "boss_slayer", "speed_demon", "perfectionist"
        }
    }

    for player, achievements in players_data.items():
        print(f"Player {player} achievements: {achievements}")

    sets = list(players_data.values())

    uniq = set().union(*sets)

    common = sets[0].intersection(*sets[1:])

    rare = set()
    for name, a_set in players_data.items():
        others = set().union(*(s for n, s in players_data.items() if n != name))
        rare = rare.union(a_set.difference(others))

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {uniq}")
    print(f"Total unique achievements: {len(uniq)}", end="\n\n")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")


if __name__ == "__main__":
    main()
