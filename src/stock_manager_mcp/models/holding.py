from pydantic import BaseModel

class Holding(BaseModel):
    symbol: str
    total_holdings: float