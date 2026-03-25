purchase = float(input("Enter purchase price per share: "))
current = float(input("Enter current price: "))
quantity = float(input("Enter quantity: "))

value = (current - purchase) * quantity

print(f"Gain/Loss: {value:.2f}")