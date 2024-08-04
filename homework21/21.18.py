def compound_interest(principal, rate, times_per_year, years):
    return principal * (1 + rate / times_per_year) ** (times_per_year * years)

def loan_payment(principal, annual_rate, num_payments):
    monthly_rate = annual_rate / 12
    return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)

def investment_return(principal, rate, years):
    return principal * (1 + rate) ** years

financial_operations = {
    'compound_interest': compound_interest,
    'loan_payment': loan_payment,
    'investment_return': investment_return
}


def financial_calculator(operation, **kwargs):
    return financial_operations.get(operation)(**kwargs)

print(f"Compound Interest: ${financial_calculator('compound_interest', principal=1000, rate=0.05, times_per_year=4, years=10)}")

print(f"Loan Payment: ${financial_calculator('loan_payment', principal=25000, annual_rate=0.07, num_payments=60)}")

print(f"Investment Return: ${financial_calculator('investment_return', principal=5000, rate=0.08, years=15)}")

