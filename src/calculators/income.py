from decimal import Decimal, ROUND_HALF_UP
from ..models.property import PropertyInput

def gross_potential_income(prop: PropertyInput) -> Decimal:
    """GPI = units * market_rent_per_unit * 12"""
    return (prop.units * prop.market_rent_per_unit * Decimal('12')).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP
    )

def effective_gross_income(prop: PropertyInput, gpi: Decimal) -> Decimal:
    """EGI = GPI * (1 - vacancy - bad debt)"""
    deduction = prop.vacancy_rate + prop.bad_debt_rate
    return (gpi * (Decimal('1') - deduction)).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP
    )