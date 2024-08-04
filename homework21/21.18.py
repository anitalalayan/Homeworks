def compound_interest(principal, rate, time, times_compounded):
    return principal * (1 + rate / times_compounded) ** (times_compounded * time)

def loan_payment(principal, annual_rate, periods):
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        return principal / periods
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -periods)

def investment_return(principal, annual_rate, years, contributions):
    future_value = principal * (1 + annual_rate) ** years
    if annual_rate != 0:
        future_value += contributions * (((1 + annual_rate) ** years - 1) / annual_rate)
    else:
        future_value += contributions * years
    return future_value

# these formulas are taken from internet, the minimal work left is done by me

financial_functions = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return
}

def financial_calculator(operation, **kwargs):
    return financial_functions.get(operation)(**kwargs)


print(financial_calculator('compound_interest', principal=1000, rate=0.05, time=10, times_compounded=4))

print(financial_calculator('loan_payment', principal=25000, annual_rate=0.06, periods=60))

print(financial_calculator('investment_return', principal=5000, annual_rate=0.07, years=15, contributions=500))
