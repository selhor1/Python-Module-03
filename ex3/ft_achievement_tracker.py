def main() -> None:

    print("=== Achievement Tracker System ===\n")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon",
                   "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    alice_unique_all = alice.difference(bob.union(charlie))
    bob_unique_all = bob.difference(alice.union(charlie))
    charlie_unique_all = charlie.difference(alice.union(bob))

    rare = alice_unique_all.union(bob_unique_all).union(charlie_unique_all)
    print(f"Rare achievements (1 player): {rare}\n")

    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")

    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
