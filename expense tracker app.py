expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        print("\n--- Expense Details ---")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for e in expenses:
                print("Name:", e["name"])
                print("Amount: Rs.", e["amount"])
                print("Category:", e["category"])
                print("-------------------")

    elif choice == "3":
        total = 0

        for e in expenses:
            total = total + e["amount"]

        print("Total Expenses: Rs.", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")