from decimal import Decimal, ROUND_HALF_UP
from ..models.property import PropertyInput

def operating_expenses(prop: PropertyInput, egi: Decimal) -> Decimal:
    """OpEx = (EGI * op_exp_pct) + tax + insurance"""
    variable = egi * prop.operating_expenses_pct
    fixed = prop.property_tax_annual + prop.insurance_annual
    return (variable + fixed).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def net_operating_income(egi: Decimal, opex: Decimal) -> Decimal:
    """NOI = EGI - OpEx"""
    return (egi - opex).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)