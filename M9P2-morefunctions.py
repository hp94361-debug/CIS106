def compute_price(msrp, make, model, electric_code):
    make = make.lower()
    model = model.lower()
    electric_code = electric_code.upper()

    # Determine discount
    if electric_code == "Y":
        discount_percent = 0.30
    elif make == "honda" and model == "accord":
        discount_percent = 0.10
    elif make == "toyota" and model == "rav4":
        discount_percent = 0.15
    else:
        discount_percent = 0.05

    discount_amount = msrp * discount_percent
    discounted_price = msrp - discount_amount

    tax = discounted_price * 0.07
    total_price = discounted_price + tax

    return total_price


def main():
    total_msrp = 0
    total_sales_price = 0

    while True:
        cont = input("Do you want to continue? (Yes/No): ").lower()
        if cont != "yes":
            break

        make = input("Enter make: ")
        model = input("Enter model: ")
        electric = input("Is it electric? (Y/N): ")
        msrp = float(input("Enter MSRP: "))

        final_price = compute_price(msrp, make, model, electric)

        total_msrp += msrp
        total_sales_price += final_price

        print(f"Make: {make}")
        print(f"Model: {model}")
        print(f"Final Price (Out the Door): {final_price:.2f}")
        print("-" * 40)

    print(f"Total MSRP of all cars: {total_msrp:.2f}")
    print(f"Total Sales Price of all cars: {total_sales_price:.2f}")


main()
