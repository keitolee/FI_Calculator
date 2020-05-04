
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


def future_inf_expenses( age, ret_age, expense, ret_years ):
    
    years_until_ret = ret_age - age
    fut_exp = inflation( expense, years_until_ret )

    total = inf_expenses( fut_exp, ret_years)

    return total