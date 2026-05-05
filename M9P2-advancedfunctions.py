def compute_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


def main():
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    score3 = float(input("Enter exam score 3: "))

    total_points, avg_score = compute_scores(score1, score2, score3)

    print(f"Student: {last_name}")
    print(f"Total Points: {total_points:.2f}")
    print(f"Average Score: {avg_score:.2f}")


main() 