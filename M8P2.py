total = 0
count = 0

file = open("orders.txt", "r")

while True:
    item = file.readline().strip()
    
    if item == "":
        break
    
    quantity = int(file.readline().strip())
    price = float(file.readline().strip())

    extended = quantity * price

    total += extended
    count += 1

    print(f"{item} Qty:{quantity} Price:{price:.2f} Extended:{extended:.2f}")

file.close()

average = total / count

print(f"Total: {total:.2f}")
print(f"Number of Orders: {count}")
print(f"Average Order: {average:.2f}")