from game import configure_match

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


if __name__ == "__main__":

    main()