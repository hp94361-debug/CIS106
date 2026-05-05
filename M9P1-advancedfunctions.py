def compute_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return discount_amount, discounted_price


def main():
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    discount_rate = float(input("Enter discount rate (e.g. 0.10 for 10%): "))

    discount, final_price = compute_discount(quantity, price, discount_rate)

    print(f"Quantity: {quantity}")
    print(f"Price: {price:.2f}")
    print(f"Discount Amount: {discount:.2f}")
    print(f"Discounted Price: {final_price:.2f}")


main() 