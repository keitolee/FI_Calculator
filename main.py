
def add_assets( cash, equity, bonds, RE, otherA ):
    return cash + equity + bonds + RE + otherA

def add_liabilities( stu_loans, mort, credit, per_loans, otherL ):
    return stu_loans + mort + credit + per_loans + otherL


cash = 10000
equity = 30000
bonds = 10000
RE = 0
otherA = 10000

stu_loans = 30000
mort = 0
credit = 2000
per_loans = 0
otherL = 0


curr_assets = add_assets ( cash, equity, bonds, RE, otherA )
curr_liabilities = add_liabilities( stu_loans, mort, credit, per_loans, otherL )


print("Total Current Assets: ", curr_assets)
print("Total Current Liabilities: ", curr_liabilities)