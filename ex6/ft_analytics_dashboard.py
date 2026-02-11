def main() -> None:

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2300]
    achievements = {
        "alice": ["first_kill", "level_10", "treasure_hunter", "speed_demon", "boss_slayer"],
        "bob": ["first_kill", "level_5", "collector"],
        "charlie": ["level_10", "boss_slayer", "speed_demon", "perfectionist", "treasure_hunter", "level_5", "first_kill"],
        "diana": ["boss_slayer", "level_10", "speed_demon"]
    }
    regions = ["north", "east", "central", "north"]

    # === Analytics Dashboard ===
    print("=== Game Analytics Dashboard ===")

    # === List Comprehension Examples ===
    print("\n=== List Comprehension Examples ===")

    # High scorers > 2000
    high_scorers = [players[i] for i in range(len(players)) if scores[i] > 2000]
    print("High scorers (>2000):", high_scorers)

    # Scores doubled
    scores_doubled = [score * 2 for score in scores]
    print("Scores doubled:", scores_doubled)

    # Active players (score > 0)
    active_players = [players[i] for i in range(len(players)) if scores[i] > 0]
    print("Active players:", active_players)

    # === Dict Comprehension Examples ===
    print("\n=== Dict Comprehension Examples ===")

    # Player scores mapping
    player_scores = {players[i]: scores[i] for i in range(len(players))}
    print("Player scores:", player_scores)

    # Score categories
    score_categories = {
        "high": len([s for s in scores if s > 2000]),
        "medium": len([s for s in scores if 1800 <= s <= 2000]),
        "low": len([s for s in scores if s < 1800])
    }
    print("Score categories:", score_categories)

    # Achievement counts
    achievement_counts = {player: len(achievements[player]) for player in players}
    print("Achievement counts:", achievement_counts)

    # === Set Comprehension Examples ===
    print("\n=== Set Comprehension Examples ===")

    # Unique players
    unique_players = {player for player in players}
    print("Unique players:", unique_players)

    # Unique achievements
    unique_achievements = {ach for ach_list in achievements.values()
                           for ach in ach_list}
    print("Unique achievements:", unique_achievements)

    # Active regions
    active_regions = {region for region in regions}
    print("Active regions:", active_regions)

    # === Combined Analysis ===
    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / len(scores)
    top_player_index = scores.index(max(scores))
    top_player = players[top_player_index]
    top_player_achievements = len(achievements[top_player])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(f"Top performer: {top_player} ({scores[top_player_index]} points, "
          f"{top_player_achievements} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected Error: {e}")
