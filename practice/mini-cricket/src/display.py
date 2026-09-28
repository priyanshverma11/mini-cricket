def display_score(
    score: int,
    wickets_lost: int,
    balls: int,
) -> None:
    overs = f"{balls // 6}.{balls % 6}"

    print()
    print("--------------------------------")
    print(f"Score : {score}/{wickets_lost}")
    print(f"Overs : {overs}")
    print("--------------------------------")


def display_match_summary(
    score: int,
    wickets_lost: int,
    balls: int,
    target: int,
) -> None:
    overs = f"{balls // 6}.{balls % 6}"

    print()
    print("=" * 32)
    print("         MATCH SUMMARY")
    print("=" * 32)
    print(f"Target      : {target}")
    print(f"Final Score : {score}/{wickets_lost}")
    print(f"Overs       : {overs}")

    if score >= target:
        print("Result      : 🏆 YOU WON!")
    else:
        print("Result      : ❌ YOU LOST!")

    print("=" * 32)