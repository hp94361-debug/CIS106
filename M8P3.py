total_tuition = 0
count = 0

file = open("students.txt", "r")

while True:
    name = file.readline().strip()
    
    if name == "":
        break
    
    code = file.readline().strip()
    credits = int(file.readline().strip())

    if code == "I":
        cost = 250
    else:
        cost = 500

    tuition = credits * cost

    total_tuition += tuition
    count += 1

    print(f"{name} Credits:{credits} Tuition:{tuition:.2f}")

file.close()

print(f"Total Tuition: {total_tuition:.2f}")
print(f"Number of Students: {count}")