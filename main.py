from func import *

cash = 15000
equity = 90000
bonds = 10000
RE = 0
otherA = 10000

stu_loans = 30000
mort = 0
credit = 2000
per_loans = 0
otherL = 0

salary = 100000
eq_returns = (equity * 0.07)/12 
cash_int = (cash * 0.02)/12 
otherI = 200

rent = 700
food = 200
utilities = 100
car = 300
otherE = 150

desired_retirement_expenses = 1500
desired_retirement_length = 35




curr_assets = add_assets ( cash, equity, bonds, RE, otherA )
curr_liabilities = add_liabilities( stu_loans, mort, credit, per_loans, otherL )

print("Total Current Assets: ", curr_assets)
print("Total Current Liabilities: ", curr_liabilities)




monthly_income = add_income( salary, eq_returns, cash_int, otherI )
monthly_expenses = add_expenses( rent, food, utilities, car, otherE )

print("Total Monthly Income: ", curr_assets)
print("Total Monthly Expenses: ", curr_liabilities)



retirement_total = inf_expenses( desired_retirement_expenses, desired_retirement_length )


# #Option 1: Retire Now

# if monthly_income <= monthly_expenses:
#     print("Income is less than expenses therefore, unable to build wealth. \n Start by increasing income and/or lowering expenses" )
# else:
#     print( "Total amout required to save for", desired_retirement_length, " years at", desired_retirement_expenses, "a month to retire TODAY: $", retirement_total )

#     if curr_assets < retirement_total:
#         print( "You are $", ( retirement_total-curr_assets ), "short of retirement")
#     else:
#         print( "Congratulations! You can retire today with an extra $", ( curr_assets-retirement_total ))


#Option 2: Retire Later

current_age = 20
retirement_age = 65

