def display_data(names, scores):
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")


def display_data_reverse(names, scores):
    i = len(names) - 1
    while i >= 0:
        print(f"{names[i]} - {scores[i]}")
        i -= 1


def main():
    names = ["Abraham", "Banks", "Cadden", "Davison", "Jacque",
             "Patel", "Hilton", "Kardashian", "Antison", "Swift"]

    scores = [88, 92, 79, 85, 90, 87, 93, 76, 84, 91]

    print("Student Scores:")
    display_data(names, scores)

    print("\nStudent Scores in Reverse:")
    display_data_reverse(names, scores)


main() 