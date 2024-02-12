import json
import os
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(list)
        self.categories = set()

    def add_expense(self, amount, description, category):
        self.expenses[category].append({"amount": amount, "description": description})
        self.categories.add(category)

    def monthly_summary(self):
        total_expenses = sum(sum(item['amount'] for item in expenses) for expenses in self.expenses.values())
        return f"Total monthly expenses: ${total_expenses:.2f}"

    def category_summary(self):
        summary = ""
        for category, expenses in self.expenses.items():
            total_expenses = sum(item['amount'] for item in expenses)
            summary += f"{category.capitalize()}: ${total_expenses:.2f}\n"
        return summary

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)

    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.expenses = defaultdict(list, json.load(file))
                for category in self.expenses.keys():
                    self.categories.add(category)

def get_valid_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    expense_tracker = ExpenseTracker()
    data_file = "expenses.json"
    expense_tracker.load_data(data_file)

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")

        choice = get_valid_input("Enter your choice: ", int)

        if choice == 1:
            amount = get_valid_input("Enter the amount spent: $", float)
            description = input("Enter a brief description: ")
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, description, category)
            expense_tracker.save_data(data_file)
            print("Expense added successfully!")

        elif choice == 2:
            print(expense_tracker.monthly_summary())

        elif choice == 3:
            print(expense_tracker.category_summary())

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
