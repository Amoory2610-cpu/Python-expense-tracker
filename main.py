from expense_manager import add_expense, view_expenses, total_expenses

def main():
    while True:
        print("1. Add Expense")
        print("2. View expense")
        print("3. total_expenses")
        print("4. exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount:"))
            category = input("Enter category: ")
            add_expense(amount, category)


        elif choice == "2":
            view_expenses()

        elif choice == "4":
            total_expenses()


        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()