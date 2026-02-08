def get_all_unique_achievements(
    players_data: dict[str, set]
) -> set:
    """
    Gather every unique achievement across all players.

    Args:
        players_data: Dictionary with player names and their sets.

    Returns:
        A set containing all unique achievements found.
    """
    all_ach: set = set()

    for achievements in players_data.values():
        all_ach = all_ach.union(achievements)

    return all_ach


def get_common_to_all(
    players_data: dict[str, set]
) -> set:
    """
    Find achievements that every single player has unlocked.

    Args:
        players_data: Dictionary with player names and their achievement sets.

    Returns:
        A set of achievements common to all players.
    """
    if not players_data:
        return set()

    sets_list = list(players_data.values())
    common = sets_list[0]

    for other_set in sets_list[1:]:
        common = common.intersection(other_set)

    return common


def get_rare_achievements(
    players_data: dict[str, set]
) -> set:
    """
    Identify achievements held by exactly one player.

    Args:
        players_data: Dictionary with player names and their sets.

    Returns:
        A set of rare achievements.
    """
    rare: set = set()

    for name, ach in players_data.items():
        others: set = set().union(
            *(s for n, s in players_data.items() if n != name)
        )
        rare = rare.union(ach.difference(others))

    return rare


def diff_in_two_players(
    p1_name: str, p1_ach: set,
    p2_name: str, p2_ach: set
) -> None:
    """
    Compare achievements between two specific players.

    Args:
        p1_name: Name of the first player.
        p1_ach: Achievement set of the first player.
        p2_name: Name of the second player.
        p2_ach: Achievement set of the second player.
    """
    print(f"{p1_name} vs {p2_name} common: {p1_ach.intersection(p2_ach)}")
    print(f"{p1_name} unique: {p1_ach.difference(p2_ach)}")
    print(f"{p2_name} unique: {p2_ach.difference(p1_ach)}")


def achievement_tracker() -> None:
    """Initialize dynamic player data and display analytics."""
    players: dict[str, set] = {
        'Chaos': {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
        'Spasha': {'first_kill', 'level_10', 'boss_slayer', 'collector'},
        'Darius': {
            'level_10', 'treasure_hunter', 'boss_slayer', 'perfectionist'
        }
    }

    print("=== Achievement Tracker System ===\n")
    for name, achs in players.items():
        print(f"Player {name} achievements: {achs}")

    try:
        all_unique = get_all_unique_achievements(players)
    except Exception as e:
        print(f"Unexpected error while getting unique achivements. {e}")

    try:
        common = get_common_to_all(players)
    except Exception as e:
        print(f"Unexpected error while getting achivements common to all. {e}")

    try:
        rare = get_rare_achievements(players)
    except Exception as e:
        print(f"Unexpected error while getting rare achivements. {e}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {rare}")

    try:
        diff_in_two_players(
            "Chaos", players['Chaos'], "Spasha", players['Spasha']
        )
    except Exception as e:
        print(
            "Unexpected error while "
            f"getting the difference of two player-sets. {e}"
        )


if __name__ == "__main__":
    achievement_tracker()
