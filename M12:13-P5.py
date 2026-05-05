def compute_student_averages(data):
    result = []

    for name in data:
        grades = data[name]
        total = 0

        for g in grades:
            total += g

        avg = total / len(grades)
        result.append([name, avg])

    return result


def compute_class_grade_averages(data):
    totals = [0, 0, 0]
    count = len(data)

    for grades in data.values():
        for i in range(3):
            totals[i] += grades[i]

    return [totals[i] / count for i in range(3)]


def main():
    students = {
        "Abrham": [80, 85, 90],
        "Banks": [90, 92, 88],
        "Cadden": [70, 75, 80],
        "Davison": [85, 87, 89]
    }

    student_avgs = compute_student_averages(students)
    class_avgs = compute_class_grade_averages(students)

    print("Student     Average")
    print("------------------------")
    for item in student_avgs:
        print(f"{item[0]:<10} {item[1]:.2f}")

    print("\nClass Averages (Exam 1, 2, 3):")
    for i in range(3):
        print(f"Exam {i+1}: {class_avgs[i]:.2f}")


main()