class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate
        return bonus


def main():
    emp = Employee("John", "Smith", 50000)

    print(f"Employee: {emp.first_name} {emp.last_name}")
    print(f"Salary: {emp.salary}")

    rate = float(input("Enter bonus rate (e.g. 0.10 for 10%): "))
    bonus = emp.compute_bonus(rate)

    print(f"Bonus: {bonus:.2f}")


main() 