def load_players(filename):
    players = {}

    file = open(filename, "r")
    for line in file:
        parts = line.strip().split()
        players[parts[0]] = float(parts[1])
    file.close()

    return players


def display_players(players):
    print("Player     Average")
    print("----------------------")

    for name in players:
        print(f"{name:<10} {players[name]:.3f}")


def main():
    players = load_players("players.txt")
    display_players(players)


main() 