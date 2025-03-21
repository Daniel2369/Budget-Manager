# Import functions module
import functions

# Storage data lists
incomes: list = [
    {"amount": 1000, "description": "Salary"},
    {"amount": 200, "description": "Freelance work"}
]

expenses: list = [
    {"amount": 500, "description": "Rent"},
    {"amount": 100, "description": "Utilities"}
]

# Main function
def main():
    global incomes, expenses  # Ensure we modify the global lists

    while True:  # Allow continuous menu run, until the user decides to exit
        print("\n===== User Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transaction History")
        print("5. Exit :) ")

        user_choice: str = input("Please choose an option from the menu (1-5): ")

        match user_choice:
            case "1":  # Add Income
                incomes, expenses = functions.add_income(incomes, expenses)

            case "2":  # Add Expense
                incomes, expenses = functions.add_expense(incomes, expenses)  # ✅ Calls your function!

            case "3":  # Show Balance
                functions.show_balance(incomes, expenses)

            case "4":  # Show Transaction History
                functions.show_transaction_history(incomes, expenses)

            case "5":  # Exit program
                print("Goodbye :)")
                break

            case _:  # Default case if input is invalid
                print("Please choose a valid option...")

# Run the program
if __name__ == '__main__':
    main()
