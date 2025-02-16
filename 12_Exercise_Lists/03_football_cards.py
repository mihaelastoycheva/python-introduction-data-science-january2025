team_a = []
team_b = []

for number in range(1, 12):
    team_a.append(f"A-{number}")
    team_b.append(f"B-{number}")

list_cards = input().split()

is_game_term = False

for num_index in range(len(list_cards)):
    if list_cards[num_index] in team_a:
        team_a.remove(list_cards[num_index])
    elif list_cards[num_index] in team_b:
        team_b.remove(list_cards[num_index])

    if len(team_a) < 7 or len(team_b) < 7:
        is_game_term = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if is_game_term:
    print("Game was terminated")
