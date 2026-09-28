from game import (configure_match,get_overs_completed,increment_ball,play_ball,update_score)

def main():

    print("=" * 32)

    print("        MINI CRICKET")

    print("=" * 32)

    overs, wickets, target = configure_match()

    print()

    print(f"Overs   : {overs}")

    print(f"Wickets : {wickets}")

    print(f"Target  : {target}")

    score = 0

    balls = 0

    outcome = play_ball()

    score = update_score(score, outcome)

    balls = increment_ball(balls)

    completed_overs = get_overs_completed(balls)

    print()

    print(f" {outcome} run(s)")

    print(f"Score : {score}")

    print(f"Balls : {balls}")

    print(f"Overs : {completed_overs}")

if __name__ == "__main__":

    main()
