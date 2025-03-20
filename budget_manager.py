# import func_module


# Storage data lists
incomes: list = [
 {"amount": 1000, "description": "Salary"},
 {"amount": 200, "description": "Freelance work"}
]

expenses: list = [
 {"amount": 500, "description": "Rent"},
 {"amount": 100, "description": "Utilities"}
]


# main function
def main():
    while True: # allow continues menu run, until the user decides to exit the program
        print("\n===== User Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show balance")
        print("4. Show Transaction History")
        print(r"5. Exit :) ")

        user_choise: str = input("Please choose an option from the menu by number: 1-5 \n") # allow user to choose an option from the menu
        match user_choise: # menu match-case
            case "1": # Option No.1 Display all invetory items
                #func_module.display_inventory_items(inventory)
            
            case "2": # Option No.2 Calculate the total inventory value
                #func_module.calculate_total_inventory_value(inventory)
            
            case "3": # Option No.3 Add a new product to inventory
                #product: str = input("Which product would you like to add to the inventory? i.e: toy 100 100 \n")
                #func_module.add_new_product(inventory,product)

            case "4": # Option No.4 Remove item from inventory
                #product: str = input("Which product would you like to remove from the inventory? \n")
                #func_module.remove_item_from_inventory(inventory,product)

            case "5":
                #print(r"Goodbye :)")
                #break

            case _: # Default use case if no valid option inserted by the user, return to the main menu
                #print("Please choose a valid option...")


if __name__ == '__main__':
    main()