import random

def configure_match() -> tuple[int, int, int]:
    overs = int(input("Enter number of overs: "))
    wickets = int(input("Enter number of wickets: "))
    target = int(input("Enter target score: "))

    return overs, wickets, target

def get_batting_strategy() -> str:
    print()
    print("Choose your shot:")
    print("1. Defensive")
    print("2. Normal")
    print("3. Aggressive")

    while True:
        strategy = input("Enter choice: ")

        if strategy in {"1", "2", "3"}:
            return strategy

        print("Please choose 1, 2, or 3.")

def play_ball(strategy: str) -> int | str:
    if strategy == "1":
        outcomes = [0, 0, 1, 1, 2, 4]
    elif strategy == "2":
        outcomes = [0, 1, 1, 2, 3, 4, 6]
    else:
        outcomes = [0, 1, 4, 4, 6, 6, "W"]

    return random.choice(outcomes)

def update_score(current_score: int, runs: int) -> int:
    return current_score + runs

def increment_ball(ball_number: int) -> int:
    return ball_number + 1

def get_overs_completed(balls: int) -> int:
    return balls // 6

def is_wicket(outcome: int | str) -> bool:
    return outcome == "W"