import pandas as pd

# Reading the raw data

raw_data = pd.read_csv('csv_reports/operating_expense.csv')

# Filtering to only extract data under "Marketing Expense"

marketing_expense_data = raw_data[raw_data['Items'] == "Marketing Expense"]

# Extracting the different "Amounts" under "Marketing Expense"

marketing_expense_amount = marketing_expense_data[['Amount']]

# Converting the data frame into a float

marketing_expense_amount = marketing_expense_amount.astype(float)

# Summimg up the different amounts

total_marketing_expense = marketing_expense_amount.sum()






# Filtering to only extract data under "Salary Expense"

salary_expense_data = raw_data[raw_data['Items'] == "Salary Expense"]

# Extracting the different "Amounts" under "Salary Expense"

salary_expense_amount = salary_expense_data[['Amount']]

# Converting the data frame into a float

salary_expense_amount = salary_expense_amount.astype(float)

# Summimg up the different amounts

total_salary_expense = salary_expense_amount.sum()






# Filtering to only extract data under "Rental Expense"

rental_expense_data = raw_data[raw_data['Items'] == "Rental Expense"]

# Extracting the different "Amounts" under "Rental Expense"

rental_expense_amount = rental_expense_data[['Amount']]

# Converting the data frame into a float

rental_expense_amount = rental_expense_amount.astype(float)

# Summimg up the different amounts

total_rental_expense = rental_expense_amount.sum()






# Filtering to only extract data under "Penalty Expense"

penalty_expense_data = raw_data[raw_data['Items'] == "Penalty Expense"]

# Extracting the different "Amounts" under "Penalty Expense"

penalty_expense_amount = penalty_expense_data[['Amount']]

# Converting the data frame into a float

penalty_expense_amount = penalty_expense_amount.astype(float)

# Summimg up the different amounts

total_penalty_expense = penalty_expense_amount.sum()






# Filtering to only extract data under "Shipping Expense"

shipping_expense_data = raw_data[raw_data['Items'] == "Shipping Expense"]

# Extracting the different "Amounts" under "Shipping Expense"

shipping_expense_amount = shipping_expense_data[['Amount']]

# Converting the data frame into a float

shipping_expense_amount = shipping_expense_amount.astype(float)

# Summimg up the different amounts

total_shipping_expense = shipping_expense_amount.sum()






# Filtering to only extract data under "Overflow Expense - Warehouse"

shipping_expense_data = raw_data[raw_data['Items'] == "Overflow Expense - Warehouse"]

# Extracting the different "Amounts" under "Overflow Expense - Warehouse"

warehouse_expense_amount = shipping_expense_data[['Amount']]

# Converting the data frame into a float

warehouse_expense_amount = warehouse_expense_amount.astype(float)

# Summimg up the different amounts

total_warehouse_expense = warehouse_expense_amount.sum()






# Filtering to only extract data under "Overflow Expense - Retail"

retail_expense_data = raw_data[raw_data['Items'] == "Overflow Expense - Retail"]

# Extracting the different "Amounts" under "Overflow Expense - Retail"

retail_expense_amount = retail_expense_data[['Amount']]

# Converting into a float

retail_expense_amount = retail_expense_amount.astype(float)

# Summimg up the different amounts

total_retail_expense = retail_expense_amount.sum()





# Filtering to only extract data under "Human Resource Expense"

hr_expense_data = raw_data[raw_data['Items'] == "Human Resource Expense"]

# Extracting the different "Amounts" under "Overflow Expense - Retail"

hr_expense_amount = hr_expense_data[['Amount']]

# Converting into a float

hr_expense_amount = hr_expense_amount.astype(float)

# Summimg up the different amounts

total_hr_expense = hr_expense_amount.sum()
