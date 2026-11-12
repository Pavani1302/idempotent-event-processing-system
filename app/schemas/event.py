from pydantic import BaseModel, Field
from decimal import Decimal

class EventRequest(BaseModel):
    event_id: str = Field(min_length=1)
    event_type: str = Field(min_length=1)
    order_id: str = Field(min_length=1)
    amount: Decimal = Field(gt = 0)