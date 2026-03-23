import csv

def add_expense(amount, category):
    with open("data/expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer = csv.writer(file)
        writer.writerow([amount, category])

