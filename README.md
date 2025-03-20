# Budget-Manager
DevOps 2025 course - Github section, practice Py program collaboration with other classmates as a team

---------------------------------------------------------------------------
# Data structure

Two separate lists for incomes and expenses,
Example:
```
incomes = [
 {"amount": 1000, "description": "Salary"},
 {"amount": 200, "description": "Freelance work"}
]
expenses = [
 {"amount": 500, "description": "Rent"},
 {"amount": 100, "description": "Utilities"}
]
```

* balance = sum(item["amount"] for item in incomes) - sum(item["amount"] for item in
  expenses)

