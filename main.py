
def add_assets( cash, equity, bonds, RE, other ):
    return cash + equity + bonds + RE + other

def add_liabilities( stu_loans, mort, credit, per_loans, other ):
    return stu_loans + mort + credit + per_loans + other


#calculates MONTHLY income

def add_income( salary, eq_int, cash_int, other ):
    return (salary/12) + eq_int + cash_int + other

#calculates MONTHLY expenses

def add_expenses( rent, food, utilities, car, other ):
     return rent + food + utilities + car + other

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
eq_int = (equity * 0.07)/12 #assuming 7% return on equities calculated yearly
cash_int = (cash * 0.02)/12 #assuming 2% return on cash calculated yearly
otherI = 200

rent = 700
food = 200
utilities = 100
car = 300
otherE = 150


curr_assets = add_assets ( cash, equity, bonds, RE, otherA )
curr_liabilities = add_liabilities( stu_loans, mort, credit, per_loans, otherL )

print("Total Current Assets: ", curr_assets)
print("Total Current Liabilities: ", curr_liabilities)

monthly_income = add_income( salary, eq_int, cash_int, otherI )
monthly_expenses = add_expenses( rent, food, utilities, car, otherE )

print("Total Monthly Income: ", curr_assets)
print("Total Monthly Expenses: ", curr_liabilities)