import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []

    i = 1
    while i < len(sys.argv):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print("Invalid score ignored:", sys.argv[i])
        i += 1

    if len(scores) == 0:
        print("No valid scores to analyze.")
        return

    print("Scores processed:", scores)
    print("Total players:", len(scores))

    total_score = sum(scores)
    print("Total score:", total_score)

    avg_score = total_score / len(scores)
    print("Average score:", avg_score)

    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught unexpected error: {e}")
