class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250
        else:
            rate = 500

        tuition = self.credits * rate
        return tuition


def main():
    student = Student("Jane", "Doe", "I", 12)

    print(f"Student: {student.first_name} {student.last_name}")
    print(f"District Code: {student.district_code}")
    print(f"Credits: {student.credits}")

    tuition = student.compute_tuition()

    print(f"Tuition Owed: {tuition:.2f}")


main()