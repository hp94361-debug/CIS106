def compute_average(grades):
    total = 0
    count = 0

    for g in grades.values():
        total += g
        count += 1

    return total / count


def main():
    students = {
        "Abraham": 88,
        "Banks": 92,
        "cadden": 79,
        "Davison": 85,
        "Jacque": 90
    }

    print("Name       Grade")
    print("--------------------")

    for name in students:
        print(f"{name:<10} {students[name]:>5}")

    avg = compute_average(students)
    print("--------------------")
    print(f"Class Average: {avg:.2f}")


main()