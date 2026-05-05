def compute_total(quantity, unit_price):
    total = quantity * unit_price
    if total > 10000:
        total *= 0.90  
    return total


def main():
    grand_total = 0

    while True:
        print("\nEnter item details (or type 0 to stop)")
        
        qty = int(input("Enter quantity: "))
        if qty == 0:
            break
        
        price = float(input("Enter unit price: "))

        total_price = compute_total(qty, price)
        grand_total += total_price

        print(f"Quantity: {qty}")
        print(f"Unit Price: {price:.2f}")
        print(f"Total Price: {total_price:.2f}")

    print(f"\nTotal Extended Price for all items: {grand_total:.2f}")


if __name__ == "__main__":
    main()
    