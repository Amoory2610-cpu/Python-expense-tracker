from expense_manager import add_expense

def main():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    add_expense(amount, category)
    print ("Saved successfully!")