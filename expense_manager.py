import csv

def add_expense(amount, category):
    with open("./data/expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])


def view_expenses():
    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            print(f"Amount: {row[0]} | Category: {row[1]}")


def total_expenses():
    total = 0

    with open("./data/expenses.csv", mode="r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            amount = float(row[0])
            total += amount

    print("Total expenses:", total)