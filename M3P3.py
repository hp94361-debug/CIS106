lastName = input("Enter last name: ")
midterm = float(input("Enter midterm score: "))
final = float(input("Enter final exam score: "))

total = (midterm * 0.40) + (final * 0.60)

print(f"Last Name: {lastName}")
print(f"Total Points: {total:.2f}")