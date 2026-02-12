import time
from typing import Generator


def game_events(n: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, n + 1):
        player = players[i % 3]
        action = actions[i % 3]
        level = (i % 15) + 1
        yield f"Event {i}: Player {player} (level {level}) {action}"


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n: int) -> Generator[int, None, None]:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    total = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    start = time.time()
    for event in game_events(total_events):
        total += 1
        print(event)
        if "found treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1
        level = int(event.split("level ")[1].split(")")[0])
        if level >= 10:
            high_level += 1
    end = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    print(", ".join(str(n) for n in fibonacci(10)))

    print("Prime numbers (first 5):", end=" ")
    print(", ".join(str(p) for p in primes(5)))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
