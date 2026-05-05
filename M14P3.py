class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        rates = {
            "I": 250,   
            "O": 500,   
            "X": 800,   
            "G": 250    
        }

        rate = rates.get(self.district_code, 500)  # default fallback
        return self.credits * rate


def main():
    students = [
        Student("Alice", "Brown", "I", 12),
        Student("Bob", "Smith", "O", 12),
        Student("Chen", "Li", "X", 12),
        Student("Maria", "Garcia", "G", 12)
    ]

    for s in students:
        print(f"{s.first_name} {s.last_name} ({s.district_code})")
        print(f"Credits: {s.credits}")
        print(f"Tuition: {s.compute_tuition():.2f}")
        print("-" * 30)


main()