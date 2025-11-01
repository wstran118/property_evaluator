import numpy_financial as npf
from decimal import Decimal

def calculate_monthly_payment(principal: Decimal, rate: Decimal, years: int) -> Decimal:
    monthly_rate = rate / 12
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    pmt = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return Decimal(pmt).quantize(Decimal('0.01'))
