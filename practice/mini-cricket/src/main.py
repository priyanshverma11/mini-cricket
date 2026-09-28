from display import display_match_summary
from game import (
    configure_match,
    get_batting_strategy,
    get_overs_completed,
    increment_ball,
    is_wicket,
    play_ball,
    update_score,
)

def main():
    print("=" * 32)
    print("       🏏 MINI CRICKET")
    print("=" * 32)

    overs, max_wickets, target = configure_match()

    print()
    print(f"Overs   : {overs}")
    print(f"Wickets : {max_wickets}")
    print(f"Target  : {target}")

    score = 0
    wickets_lost = 0
    balls = 0
    total_balls = overs * 6

    while balls < total_balls:
        strategy = get_batting_strategy()
        outcome = play_ball(strategy)

        balls = increment_ball(balls)

        if is_wicket(outcome):
            wickets_lost += 1
            print(f"\nBall {balls}: 🏏 OUT!")
        else:
            score = update_score(score, outcome)
            print(f"\nBall {balls}: 🏏 {outcome} run(s)")

        completed_overs = get_overs_completed(balls)

        print(f"Score : {score}/{wickets_lost}")
        print(f"Overs : {completed_overs}")

        if score >= target:
            break

        if wickets_lost >= max_wickets:
            break

    display_match_summary(score, wickets_lost, balls, target)

if __name__ == "__main__":
    main()