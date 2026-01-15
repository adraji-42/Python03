def diff_players(player1: list[str, set], player2: list[str, set]):

    print


def main():
    print("=== Achievement Tracker System ===", end="\n\n")

    # Data dictionary for players
    players = {
        "Chaos": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "rida2015": {"first_kill", "level_10", "boss_slayer", "collector"},
        "Spacha": {
            "level_10", "treasure_hunter",
            "boss_slayer", "speed_demon", "perfectionist"
        }
    }

    achievement_sets = []
    for player, achievements in players.items():
        print(f"Player {player} achievements: {achievements}")
        achievement_sets.append(achievements)

    # 1. All unique achievements
    unique_all = set().union(*achievement_sets)

    # 2. Common to all players
    common_all = achievement_sets[0].intersection(*achievement_sets[1:])

    # 3. Rare achievements (strictly appearing in only one set)
    rare_all = set()
    for name, current_set in players.items():
        # Combine all other players' achievements
        others = set().union(
            *(s for n, s in players.items() if n != name)
        )
        rare_all = rare_all.union(current_set.difference(others))

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {unique_all}")
    print(f"Total unique achievements: {len(unique_all)}", end="\n\n")

    print(f"Common to all players: {common_all}")
    print(f"Rare achievements (1 player): {rare_all}", end="\n\n")

    player1 = "Chaos"
    player2 = "Spacha"
    diff_players([player1, players[player1]], [player2, players[player2]])


if __name__ == "__main__":
    main()
