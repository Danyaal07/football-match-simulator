from simulator.match import simulate_match

def main():
    team_a = {"name" : "Team A", "attack": 90, "defence": 75}
    team_b = {"name" : "Team B", "attack": 75, "defence": 75}

    goals_a, goals_b = simulate_match(team_a, team_b)

    print(f"{team_a['name']} {goals_a} - {goals_b} {team_b['name']}")

if __name__ == "__main__":
    main()