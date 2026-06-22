from sys import argv


def scores_analysis(scores: list[int]) -> None:
    """
    Performs statistical analysis on a list of player scores.

    Args:
        scores (list[int]): A list of integer scores to be analyzed.
    """

    n_scores = len(scores)
    t_scores = sum(scores)
    max_scores = max(scores)
    min_scores = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {n_scores}")
    print(f"Total score: {t_scores}")
    print(f"Average score: {t_scores / n_scores:.1f}")
    print(f"High score: {max_scores}")
    print(f"Low score: {min_scores}")
    print(f"Score range: {max_scores - min_scores}", end="\n\n")


def main() -> None:
    """
    Entry point of the script that handles command-line input.
    """

    args = argv[1:]

    print("=== Player Score Analytics ===\n")
    if len(args) == 0:
        print("No scores provided.\n"
              "\tUsage: python3 ft_score_analytics.py <score1> <score2> ...",
              end="\n\n")
        return

    try:
        scores = [int(score) for score in (args)]
        if min(scores) < 0:
            print("Score cannot be negative")
            return
        scores_analysis(scores)
    except ValueError as error:
        print(f"Pleas enter a valide numbers, {error}")
    except Exception as error:
        print(f"Unexpected Erro: {error}")


if __name__ == "__main__":
    main()
