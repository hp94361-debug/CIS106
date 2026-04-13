total_bonus = 0

file = open("employees.txt", "r")

while True:
    name = file.readline().strip()
    
    if name == "":
        break
    
    salary = float(file.readline().strip())

    # Determine bonus rate
    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus += bonus

    print(f"{name} Salary: {salary:.2f} Bonus: {bonus:.2f}")

file.close()

print(f"Total Bonus Paid: {total_bonus:.2f}")