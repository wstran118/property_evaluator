from pydantic import BaseModel
from typing import List, Optional
from decial import Decimal

class RepairItem(BaseModel):
    description: str
    cost: Decimal
    urgency: str # critical, medium, cosmetic

class PropertyInput(BaseModel):
    address: str
    purchase_price: Decimal
    current_rent_per_unit: Decimal
    units: int
    market_rent_per_unit: Decimal
    cap_rate_market: Decimal
    vacancy_rate: Decimal = Decimal('0.05')
    bad_debt_rate: Decimal = Decimal('0.02')
    operating_expenses_pct: Decimal = Decimal('0.35')
    property_tax_annual: Decimal
    insurance_annual: Decimal
    repairs: List[RepairItem] = []
    loan_amount: Optional[Decimal] = None
    interest_rate: Decimal
    loan_term_years: int = 30
    hold_period_years: int = 5
    appreciation_rate: Decimal = Decimal('0.03')
    exit_cap_rate: Decimal = None  # if None, use entry + 0.5%