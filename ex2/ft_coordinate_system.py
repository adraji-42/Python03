from math import sqrt


def position_parsing(coordinates: str) -> tuple[int, int, int]:
    """
    Convert a comma-separated string into a 3D coordinate tuple.

    Args:
        coordinates (str): A string containing three integers separated
            by commas (e.g., "10,20,30").

    Returns:
        tuple: A tuple of three integers (x, y, z).
    """

    parts = coordinates.split(",")

    if len(parts) != 3:
        raise ValueError(
                "Error in coordinate parsing:\n"
                "Expected 3 values separated by commas, like: 'x,y,z'."
            )

    try:
        position = tuple([int(part) for part in parts])
    except ValueError as error:
        raise ValueError(
                "Error in coordinate parsing:\n"
                f"Error details - Type: ValueError | Error: {error}"
            )

    print(f"Parsed position: {position}")
    return position


def calculating_distance(
            position1: tuple[int, int, int], position2: tuple[int, int, int]
            ) -> float:
    """
    Calculates the Euclidean distance between two points in 3D space.

    Args:
        position1 (tuple[int, int, int]):
        The (x, y, z) coordinates of the first point.
        position2 (tuple[int, int, int]):
        The (x, y, z) coordinates of the second point.

    Returns:
        float: The straight-line distance between the two points.
    """
    x1, y1, z1 = position1
    x2, y2, z2 = position2

    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    """
    Demonstrates coordinate parsing, distance calculation, and error handling.
    """

    print("=== Game Coordinate System ===", end="\n\n")

    origin = (0, 0, 0)
    coordinates = (10, 20, 5)

    print(f"Position created: {coordinates}")

    try:
        print(
            f"Distance between {origin} and {coordinates}:"
            f"{calculating_distance(origin, coordinates):.1f}\n"
        )
    except ValueError as error:
        print(f"Error {error}")
    except Exception as error:
        print(f"Unexpected Erro: {error}")

    str_coordinate = "3,4,0"
    print(f"Parsing coordinates: \"{str_coordinate}\"")
    try:
        position = position_parsing(str_coordinate)
    except ValueError as error:
        print(f"Error {error}")
    except Exception as error:
        print(f"Unexpected Erro: {error}")
    else:
        try:
            print(
                f"Distance between {origin} and {position}:"
                f"{calculating_distance(origin, position):.1f}\n"
            )
        except ValueError as error:
            print(f"Error {error}")
        except Exception as error:
            print(f"Unexpected Erro: {error}")

    bad_coordinates = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_coordinates}\"")
    try:
        position = position_parsing(bad_coordinates)
    except ValueError as error:
        print(f"Error {error}", end="\n\n")
    except Exception as error:
        print(f"Unexpected Erro: {error}")
    else:
        try:
            print(
                f"Distance between {origin} and {position}:"
                f"{calculating_distance(origin, position):.1f}\n"
            )
        except ValueError as error:
            print(f"Error {error}")
        except Exception as error:
            print(f"Unexpected Erro: {error}")

    print("Unpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
