from simulator.match import simulate_match

def main():
    teams = [
    {"name": "Barcelona", "attack": 90, "defence": 80},
    {"name": "Manchester City", "attack": 85, "defence": 75},
    {"name": "Real Madrid", "attack": 80, "defence": 85},
    {"name": "Liverpool", "attack": 75, "defence": 70},
]
    
    match_results = []
    team_stats = {team['name']: {'points': 0, 'goals_for': 0, 'goals_against': 0} for team in teams}
    for _ in range(2):  # Each team plays against every other team twice (home and away)
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                team_a = teams[i]
                team_b = teams[j]
                goals_a, goals_b = simulate_match(team_a, team_b)
                if goals_a > goals_b:
                    match_results.append((team_a['name'], team_b['name'], goals_a, goals_b))
                    team_stats[team_a['name']]['points'] += 3
                    team_stats[team_a['name']]['goals_for'] += goals_a
                    team_stats[team_b['name']]['goals_against'] += goals_a
                elif goals_b > goals_a:
                    match_results.append((team_b['name'], team_a['name'], goals_b, goals_a))
                    team_stats[team_b['name']]['points'] += 3
                    team_stats[team_b['name']]['goals_for'] += goals_b
                    team_stats[team_a['name']]['goals_against'] += goals_b
                else:
                    match_results.append((team_a['name'], team_b['name'], goals_a, goals_b))
                    team_stats[team_a['name']]['points'] += 1
                    team_stats[team_b['name']]['points'] += 1
                    team_stats[team_a['name']]['goals_for'] += goals_a
                    team_stats[team_b['name']]['goals_for'] += goals_b
                    team_stats[team_a['name']]['goals_against'] += goals_b
                    team_stats[team_b['name']]['goals_against'] += goals_a
                print(f"{team_a['name']} {goals_a} - {goals_b} {team_b['name']}")

    print("\nFinal Standings:")
    standings = sorted(team_stats.items(), key=lambda x: (x[1]['points'], x[1]['goals_for'] - x[1]['goals_against']), reverse=True)
    for rank, (team_name, stats) in enumerate(standings, start=1):
        print(f"{rank}. {team_name} - Points: {stats['points']}, Goals For: {stats['goals_for']}, Goals Against: {stats['goals_against']}")

    

if __name__ == "__main__":
    main()

