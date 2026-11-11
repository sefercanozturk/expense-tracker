expenses = []

while True:
    amount_input = input("Amount (€) or 'q' to quit: ")
    if amount_input == "q":
        break
    amount = float(amount_input)
    category = input("Category: ")
    expenses.append((category, amount))

print("\nYour expenses:")
total = 0
for category, amount in expenses:
    print(f"{category}: {amount:.2f} €")
    total += amount

print(f"Total: {total:.2f} €")
