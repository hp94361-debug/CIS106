answer = input("Do you want to continue? (Yes/No): ")
count = 0

while answer.lower() == "yes":
    lastName = input("Enter last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

    average = (exam1 + exam2) / 2

    print(f"{lastName} Average: {average:.2f}")

    count += 1

    # Ask again INSIDE loop
    answer = input("Do you want to continue? (Yes/No): ")

print(f"Number of students entered: {count}")