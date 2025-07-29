DeprecationWarning# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 310,
    "AMZN": 140
}

portfolio = {}
total_value = 0

print(" Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("Enter stock name and quantity. Type 'done' to finish.\n")

# Taking user input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(" Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print(" Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print(" Please enter a valid number.")

# Display portfolio summary
print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock} - Qty: {qty}, Price: ${price}, Total: ${value}")

print(f"\n Total Investment Value: ${total_value}")

# Ask user if they want to save the result
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    try:
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                file.write(f"{stock},{qty},{price},{value}\n")
            file.write(f"\nTotal Investment,,,{total_value}\n")
        print(f" Portfolio saved to '{filename}'")
    except Exception as e:
        print(" Error saving file:", e)
