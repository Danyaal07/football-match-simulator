def simulate_match(team_a, team_b):
    import random
    attack_a = team_a['attack']
    attack_b = team_b['attack']
    defence_a = team_a['defence']
    defence_b = team_b['defence']

    shots_a = random.randint(0, attack_a // 10)
    shots_b = random.randint(0, attack_b // 10)

    saved_a = random.randint(0, defence_a // 10)
    saved_b = random.randint(0, defence_b // 10)


    return max(0, shots_a - saved_a), max(0, shots_b - saved_b)