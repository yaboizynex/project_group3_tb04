from pathlib import Path
import re, csv
from turtle import pen

# Creating file path & reading the file

path = Path(r"C:\Users\ganes\OneDrive\Desktop\project_group3_tb04\csv_reports\Overheads.csv")
with path.open(mode="r", encoding="CP1252") as file:
    data = file.read()

# Extracting the data for salary expense

salary_expense = (re.findall(pattern="Salary Expense.+", string=data))[0]
salary_expense = salary_expense.split(',')
salary_expense = salary_expense[1]

# Converting the string into a float

salary_expense = float(salary_expense)

# Extracting the data for interest expense

interest_expense = (re.findall(pattern="Interest Expense.+", string=data))[0]
interest_expense = interest_expense.split(',')
interest_expense = interest_expense[1]

# Converting the string into a float

interest_expense = float(interest_expense)

# Extracting the data for marketing expense

marketing_expense = (re.findall(pattern="Marketing Expense.+", string=data))[0]
marketing_expense = marketing_expense.split(',')
marketing_expense = marketing_expense[1]

# Converting the string into a float

marketing_expense = float(marketing_expense)

# Extracting the data for rental expense

rental_expense = (re.findall(pattern="Rental Expense.+", string=data))[0]
rental_expense = rental_expense.split(',')
rental_expense = rental_expense[1]

# Converting the string into a float

rental_expense = float(rental_expense)

# Extracting the data for overflow expense - retail

overflow_expense_retail = (re.findall(pattern="Overflow Expense - Retail.+", string=data))[0]
overflow_expense_retail = overflow_expense_retail.split(',')
overflow_expense_retail = overflow_expense_retail[1]

# Converting the string into a float

overflow_expense_retail = float(overflow_expense_retail)

# Extracting the data for overflow expense - warehouse

overflow_expense_warehouse = (re.findall(pattern="Overflow Expense - Warehouse.+", string=data))[0]
overflow_expense_warehouse = overflow_expense_warehouse.split(',')
overflow_expense_warehouse = overflow_expense_warehouse[1]

# Converting the string into a float

overflow_expense_warehouse = float(overflow_expense_warehouse)

# Extracting the data for penalty expense

penalty_expense = (re.findall(pattern="Penalty Expense.+", string=data))[0]
penalty_expense = penalty_expense.split(',')
penalty_expense = penalty_expense[1]

# Converting the string into a float

penalty_expense = float(penalty_expense)

# Extracting the data for shipping expense

shipping_expense = (re.findall(pattern="Shipping Expense.+", string=data))[0]
shipping_expense = shipping_expense.split(',')
shipping_expense = shipping_expense[1]

# Converting the string into a float

shipping_expense = float(shipping_expense)

# Extracting the data for human resource expense

human_resource_expense = (re.findall(pattern="Human Resource Expense.+", string=data))[0]
human_resource_expense = human_resource_expense.split(',')
human_resource_expense = human_resource_expense[1]

# Converting the string into a float

human_resource_expense = float(human_resource_expense)

# Loop to find out which overhead expense is the highest

if salary_expense>interest_expense and salary_expense>marketing_expense and salary_expense>rental_expense and salary_expense>overflow_expense_retail and salary_expense>overflow_expense_warehouse and salary_expense>penalty_expense and salary_expense>shipping_expense and salary_expense>human_resource_expense:
    print(f"Salary expenses are the highest overhead expense at {salary_expense}")

elif interest_expense>salary_expense and interest_expense>marketing_expense and interest_expense>rental_expense and interest_expense>overflow_expense_retail and interest_expense>overflow_expense_warehouse and interest_expense>penalty_expense and interest_expense>shipping_expense and interest_expense>human_resource_expense:
    print (f"Interest expenses are the highest overhead expense at {interest_expense}")

elif marketing_expense>salary_expense and marketing_expense>interest_expense and marketing_expense>rental_expense and marketing_expense>overflow_expense_retail and marketing_expense>overflow_expense_warehouse and marketing_expense>penalty_expense and marketing_expense>shipping_expense and marketing_expense>human_resource_expense:
    print (f"Marketing expenses are the highest overhead expense at {marketing_expense}")

elif rental_expense>salary_expense and rental_expense>interest_expense and rental_expense>marketing_expense and rental_expense>overflow_expense_retail and rental_expense>overflow_expense_warehouse and rental_expense>penalty_expense and rental_expense>shipping_expense and rental_expense>human_resource_expense:
    print (f"Rental expenses are the highest overhead expense at {rental_expense}")

elif overflow_expense_retail>salary_expense and overflow_expense_retail>interest_expense and overflow_expense_retail>marketing_expense and overflow_expense_retail>rental_expense and overflow_expense_retail>overflow_expense_warehouse and overflow_expense_retail>penalty_expense and overflow_expense_retail>shipping_expense and overflow_expense_retail>human_resource_expense:
    print (f"Overflow Expense - Retail is the highest overhead expense at {overflow_expense_retail}")

elif overflow_expense_warehouse>salary_expense and overflow_expense_warehouse>interest_expense and overflow_expense_warehouse>marketing_expense and overflow_expense_warehouse>rental_expense and overflow_expense_warehouse>overflow_expense_retail and overflow_expense_warehouse>penalty_expense and overflow_expense_warehouse>shipping_expense and overflow_expense_warehouse>human_resource_expense:
    print (f"Overflow Expense - Warehouse is the highest overhead expense at {overflow_expense_warehouse}")

elif penalty_expense>salary_expense and penalty_expense>interest_expense and penalty_expense>marketing_expense and penalty_expense>rental_expense and penalty_expense>overflow_expense_retail and penalty_expense>overflow_expense_warehouse and penalty_expense>shipping_expense and penalty_expense>human_resource_expense:
    print (f"Penalty expenses are the highest overhead expense at {penalty_expense}")
    
elif shipping_expense>salary_expense and shipping_expense>interest_expense and shipping_expense>marketing_expense and shipping_expense>rental_expense and shipping_expense>overflow_expense_retail and shipping_expense>overflow_expense_warehouse and shipping_expense>penalty_expense and shipping_expense>human_resource_expense:
    print (f"Shipping expenses are the highest overhead expense at {shipping_expense}")
elif human_resource_expense>salary_expense and human_resource_expense>interest_expense and human_resource_expense>marketing_expense and human_resource_expense>rental_expense and human_resource_expense>overflow_expense_retail and human_resource_expense>overflow_expense_warehouse and human_resource_expense>penalty_expense and human_resource_expense>shipping_expense:
    print (f"Human resource expenses are the highest overhead expense at {human_resource_expense}")
