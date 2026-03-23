from expense_manager import add_expense, view_expenses, total_expenses, filter_expenses_by_category, summary_by_category

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Summary by Category")
        print("6. Exit")

        choice = input("Choose an option: ").strip().lower()

        if choice in ["1", "1.", "add", "add expense"]:
            while True:
                try:
                    amount = float(input("Enter amount: "))

                    if amount <= 0:
                        print("Amount must be positive.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number.")
            while True:
                category = input("Enter category: ").strip().lower()

                if category == "":
                    print("Category cannot be empty.")
                elif category.isdigit():
                    print("Category cannot be a number.")
                else:
                    break
            add_expense(amount, category)


        elif choice in ["2", "2.", "view"]:

            view_expenses()


        elif choice in ["3", "3.", "total"]:

            total_expenses()


        elif choice in ["4", "4.", "filter"]:

            category = input("Enter category to filter: ")

            filter_expenses_by_category(category)

        elif choice in ["5", "summary"]:
            summary_by_category()


        elif choice in ["6", "6.", "exit"]:
            print("Goodbye!")
            break


        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()