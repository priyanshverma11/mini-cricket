from game import configure_match, play_ball

def main():

    print("=" * 32)

    print("        MINI CRICKET")

    print("=" * 32)

    print()

    overs, wickets, target = configure_match()

    print()

    print("Match Configuration")

    print(f"Overs: {overs}")

    print(f"Wickets: {wickets}")

    print(f"Target: {target}")

    print()

    print("Playing first ball...")

    runs = play_ball()

    print(f" You scored {runs} run(s)!")

if __name__ == "__main__":

    main()