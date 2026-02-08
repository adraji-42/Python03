from sys import argv


def main() -> None:
    """
    Processes command-line arguments and displays them to the user.

    Args:
        None (Uses sys.argv directly).
    """

    print("=== Command Quest ===\n")

    program_name, *args = argv
    args_len = len(args)

    if args_len == 0:
        print("No arguments provided!")

    print(f"Program name: {program_name}")

    if args_len > 0:
        print(f"Arguments received: {args_len}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {args_len + 1}", end="\n\n")


if __name__ == "__main__":
    main()
