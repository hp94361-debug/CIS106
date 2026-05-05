def load_data(filename):
    names = []
    scores = []

    file = open(filename, "r")
    for line in file:
        parts = line.strip().split()
        names.append(parts[0])
        scores.append(int(parts[1]))
    file.close()

    return names, scores


def find_high_low(names, scores):
    high_val = 0
    low_val = 999

    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_val:
            high_val = scores[i]
            high_index = i

        if scores[i] < low_val:
            low_val = scores[i]
            low_index = i

    return high_index, low_index


def main():
    names, scores = load_data("students.txt")

    hi, lo = find_high_low(names, scores)

    print(f"Highest Score: {names[hi]} - {scores[hi]}")
    print(f"Lowest Score: {names[lo]} - {scores[lo]}")


main() 