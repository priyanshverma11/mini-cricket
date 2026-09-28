from game import (configure_match,play_ball,update_score,increment_ball)

def main():

    print("=" * 32)

    print("        MINI CRICKET")

    print("=" * 32)

    print()

    overs, wickets, target = configure_match()

    score = 0

    print()

    print(f"Target: {target}")

    print("Playing first ball...")

    runs = play_ball()

    score = update_score(score, runs)

    print(f" You scored {runs} run(s)!")

    print(f"Score: {score}/{wickets}")

if __name__ == "__main__":

    main()