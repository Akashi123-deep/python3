
import sys

def main() -> None:
    scores : list[int] = []
    print("=== Player Score Analytics ===")
    if (len(sys.argv) > 1):
        for score in sys.argv[1:]:
            try:
                scores.append(int(score))
            except ValueError:
                print("Invalid input")
                return
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()