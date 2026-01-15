from sys import argv


def main():

    args = argv[1:]

    print("=== Player Score Analytics ===")
    if len(args) == 0:
        print("No scores provided.\n"
              "\tUsage: python3 ft_score_analytics.py <score1> <score2> ...",
              end="\n\n")
        return

    try:
        scores = []
        for arg in args:
            scores.append(int(arg))
    except ValueError:
        print("Pleas enter valide number")
        return

    number_scors = len(scores)
    totale_scors = sum(scores)
    max_scors = max(scores)
    min_scors = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {number_scors}")
    print(f"Total score: {totale_scors}")
    print(f"Average score: {totale_scors / number_scors:.1f}")
    print(f"High score: {max_scors}")
    print(f"Low score: {min_scors}")
    print(f"Score range: {max_scors - min_scors}", end="\n\n")


if __name__ == "__main__":
    main()
