def compute_forecast(month, sales):
    month = month.lower()

    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        percent = 0  

    forecast_sales = sales * (1 + percent)
    return forecast_sales


def main():
    while True:
        cont = input("Do you want to continue? (Yes/No): ").lower()
        if cont != "yes":
            break

        last_name = input("Enter last name: ")
        month = input("Enter month (Jan–Dec): ")
        sales = float(input("Enter sales: "))

        next_month_sales = compute_forecast(month, sales)

        print(f"Last Name: {last_name}")
        print(f"Month: {month}")
        print(f"Sales: {sales:.2f}")
        print(f"Next Month Forecast: {next_month_sales:.2f}")
        print("-" * 40)

 
main()  


