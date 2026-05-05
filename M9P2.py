def compute_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

def main():
    player_count = 0

    while True:
        name = input("Enter player name (or 'quit' to stop): ")
        if name.lower() == 'quit':
            break

        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))

        avg = compute_average(hits, at_bats)
        player_count += 1

        print(f"Player: {name}")
        print(f"Batting Average: {avg:.3f}")
        print("-" * 30)

    print(f"Total number of players entered: {player_count}")

main() 