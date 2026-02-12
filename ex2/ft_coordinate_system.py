import math


def create_position(x: int, y: int, z: int) -> tuple:
    return (x, y, z)


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 +
                     (y2 - y1) ** 2 +
                     (z2 - z1) ** 2)


def parse_coordinates(coord_string: str) -> None:
    try:
        parts = coord_string.split(",")
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f"Error details - Type: {type(e).__name__}, Args: {e.args}\n"
        )


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos = create_position(10, 20, 5)
    print(f"Position created: {pos}")

    origin = (0, 0, 0)
    dist = calculate_distance(origin, pos)
    print(f"Distance between {origin} and {pos}: {dist:.2f}\n")

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    parsed = parse_coordinates(coord_str)

    print(f"Parsed position: {parsed}")

    dist2 = calculate_distance(origin, parsed)
    print(f"Distance between {origin} and {parsed}: {dist2}\n")

    invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid}"')
    parse_coordinates(invalid)

    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
