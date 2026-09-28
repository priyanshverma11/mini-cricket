import random

def configure_match() -> tuple[int, int, int]:

    overs = int(input("Enter number of overs: "))

    wickets = int(input("Enter number of wickets: "))

    target = int(input("Enter target score: "))

    return overs, wickets, target

def play_ball() -> int | str:

    return random.choice([0, 1, 2, 3, 4, 6, "W"])

def update_score(current_score: int, runs: int) -> int:

    return current_score + runs

def increment_ball(ball_number: int) -> int:

    return ball_number + 1

def get_overs_completed(balls: int) -> int:

    return balls // 6

def is_wicket(outcome: int | str) -> bool:

    return outcome == "W"