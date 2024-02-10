from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import date

class AbillityImportSchema(BaseModel):
    customer_id: str = Field(..., min_length=8, max_length=12, pattern="^[0-9]+$")
    billing_sku: str = Field(..., pattern="^AB-[A-Z]+-[0-9]+$")
    activation_date: date
    monthly_charge: float = Field(..., ge=0.0)
    discount_code: Optional[str] = None

def validate_payload(data: dict):
    try:
        validated = AbillityImportSchema(**data)
        print("Schema validation passed.")
        return validated
    except ValidationError as e:
        print(f"Schema Violation detected:\n{e.json()}")

if __name__ == "__main__":
    # Test with strict enterprise rules
    mock_row = {
        "customer_id": "00482910",
        "billing_sku": "AB-CORE-100",
        "activation_date": "2026-10-01",
        "monthly_charge": 45.99
    }
    validate_payload(mock_row)
