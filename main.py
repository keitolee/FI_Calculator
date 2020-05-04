
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


#calculates compound interest   

def compound_interest( principal, rate, periods):
    total = principal * ( pow( ( 1 + rate ), periods ))
    return total

#calculates present value in given number of years due to inflation

def inflation( amount, years ):
    total = amount * pow(1.0227, years)
    return total

#calculates total current dollar value required to pay for all expenses within retirement years including inflation (sum of monthly expenses throughout retirement years)

def inf_expenses( expense, years):

    months = years*12
    mon_rate = 0.0227/12
    prev = expense
    curr = 0
    total = 0

    for i in range(months):
        curr = prev * ( 1 + mon_rate )
        total = total + curr
        prev = curr
        
    # return "{:.2f}".format(total)
    return total


# def future_inf_expenses( age, ret_age, expense, ret_years ):

    


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

print(inflation(1000,2))