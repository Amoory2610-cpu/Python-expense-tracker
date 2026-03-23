import csv

from datetime import date

def add_expense(amount, category):
    today = date.today()   # ✅ THIS LINE WAS MISSING

    with open("./data/expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, today])


def view_expenses():
    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        expenses = list(reader)

        # sort by amount (highest first)
        expenses.sort(key=lambda row: float(row[0]), reverse=True)

        for row in expenses:
            print(f"Amount: {row[0]} | Category: {row[1]} | Date: {row[2]}")

def total_expenses():
    total = 0

    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            amount = float(row[0])
            total += amount

    print("Total expenses:", total)

def filter_expenses_by_category(category):
    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        expenses = list(reader)

        filtered = list(filter(lambda row: row[1] == category, expenses))

        for row in filtered:
            print(f"Amount: {row[0]} | Category: {row[1]}")

def summary_by_category():
    summary = {}

    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            amount = float(row[0])
            category = row[1]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    for category, total in summary.items():
        print(f"{category}: {total}")