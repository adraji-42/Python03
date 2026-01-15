from sys import argv


def main():

    print("=== Command Quest ===")

    program_name, *args = argv
    len_args = len(args)

    if len_args == 0:
        print("No arguments provided!")

    print(f"Program name: {program_name}")

    if len_args > 0:
        print(f"Arguments received: {len_args}")
        i = 1
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len_args + 1}", end="\n\n")


if __name__ == "__main__":
    main()
