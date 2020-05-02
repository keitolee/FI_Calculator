
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

def compound_interest( principal, rate, periods):
    total = principal * ( pow( ( 1 + rate ), periods ) - 1 )
    return "{:.2f}".format(total)

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
eq_int = (equity * 0.07)/12 
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

monthly_income = add_income( salary, eq_int, cash_int, otherI )
monthly_expenses = add_expenses( rent, food, utilities, car, otherE )

print("Total Monthly Income: ", curr_assets)
print("Total Monthly Expenses: ", curr_liabilities)

retirement_total = ( desired_retirement_length * 12 ) * desired_retirement_expenses

if monthly_income <= monthly_expenses:
    print("Income is less than expenses therefore, unable to build wealth. \n Start by increasing income and/or lowering expenses" )
else:
    print( "Total amout required to save for ", desired_retirement_length, " years at ", desired_retirement_expenses, " a month: $", retirement_total )

 