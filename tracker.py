import csv
import os
expenses = []

while True:
    amount_input = input("Amount (€) or 'q' to quit: ")
    if amount_input.lower() == "q":
        break
    
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid input! Please enter a valid number (e.g., 15.50).")
        continue
        
    category = input("Category: ")
    expenses.append((category, amount))

print("\nYour expenses:")
total = 0
for category, amount in expenses:
    print(f"{category}: {amount:.2f} €")
    total += amount

print(f"Total: {total:.2f} €")


if expenses:
    filename = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "expenses.csv"
    )

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount"])
        for category, amount in expenses:
            writer.writerow([category, amount])
    print(f"\nData successfully saved to '{filename}'!")

