# Functions.py file module

def add_expense(incomes: list, expenses: list) -> tuple:
    """
    Adds one or more expenses to the expenses list.
    Receives:
        incomes: list of income dictionaries (not modified)
        expenses: list of expense dictionaries (will be updated)
    Returns:
        A tuple: (incomes, updated expenses)
    """
    while True:
        description = input("Enter expense description (or 'q' to quit): ")
        if description.lower() == "q":
            break
        try:
            amount = float(input("Enter expense amount: "))
            expenses.append({
                "amount": amount,
                "description": description
            })
        except ValueError:
            print("Invalid amount. Please enter a number.")
    return incomes, expenses






def add_income(incomes: list, expenses: list) -> tuple:
    while True:
        description = input("Enter income transaction description (or 'q' to quit): ")
        if description.lower() == "q":
            break
        try:
            amount = float(input("Enter income transaction amount: "))
            incomes.append({"amount": amount, "description": description})
        except ValueError:
            print("Error: Invalid amount. Please enter a valid number.")
    
    return incomes, expenses




def show_balance(incomes: list, expenses: list) -> tuple:
    balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in expenses)
    print(f"Your balance is ₪ {balance}")

    return incomes, expenses



def show_transaction_history(incomes: list, expenses: list) -> tuple:
    print("Transaction History:\n")
    print("Incomes Transactions:")
    for item in incomes:
        print(f"Amount: {item["amount"]} ₪, Description: {item["description"]}")

    print("\nExpenses Transactions:")
    for item in expenses:
        print(f"Amount: {item["amount"]} ₪, Description: {item["description"]}")

    return incomes, expenses




