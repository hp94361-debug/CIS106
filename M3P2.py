symbol = input("enter stick ticker symbol: ")
shares = float(input("Enter number of shares: "))
price = float(input("Enter cost per share: "))
investment = shares * price 
print(f"stock: {symbol}")
print(f"Total investment: {investment:.2f}")


