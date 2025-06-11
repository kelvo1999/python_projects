import csv
import os
from datetime import datetime

class BudgetTracker:
    def __init__(self, csv_file="transactions.csv"):
        self.csv_file = csv_file
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        """Load transactions from CSV file."""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                self.transactions = [
                    {"type": row["type"], "description": row["description"], 
                     "amount": float(row["amount"]), "date": row["date"]}
                    for row in reader
                ]

    def save_transactions(self):
        """Save transactions to CSV file."""
        with open(self.csv_file, mode="w", newline="") as file:
            fieldnames = ["type", "description", "amount", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.transactions)

    def add_income(self, description, amount):
        """Add an income transaction."""
        self.transactions.append({
            "type": "income",
            "description": description,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_transactions()

    def add_expense(self, description, amount):
        """Add an expense transaction."""
        self.transactions.append({
            "type": "expense",
            "description": description,
            "amount": -amount,  # Store expenses as negative
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_transactions()

    def get_balance(self):
        """Calculate the current balance."""
        return sum(transaction["amount"] for transaction in self.transactions)

    def display_transactions(self):
        """Display all transactions."""
        if not self.transactions:
            print("\nNo transactions found.")
            return
        print("\nTransaction History:")
        print("-" * 50)
        print(f"{'Type':<10} {'Description':<20} {'Amount':<10} {'Date':<20}")
        print("-" * 50)
        for t in self.transactions:
            print(f"{t['type'].capitalize():<10} {t['description']:<20} {t['amount']:<10.2f} {t['date']:<20}")

def main():
    tracker = BudgetTracker()
    
    while True:
        print("\n=== Simple Budget Tracker ===")
        print(f"Current Balance: ${tracker.get_balance():.2f}")
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            description = input("Enter income description: ")
            try:
                amount = float(input("Enter income amount: "))
                if amount <= 0:
                    print("Amount must be positive!")
                else:
                    tracker.add_income(description, amount)
                    print(f"Added income: ${amount:.2f}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        elif choice == "2":
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    print("Amount must be positive!")
                else:
                    tracker.add_expense(description, amount)
                    print(f"Added expense: ${amount:.2f}")
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        elif choice == "3":
            tracker.display_transactions()
        
        elif choice == "4":
            print("Thank you for using the Budget Tracker! Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()