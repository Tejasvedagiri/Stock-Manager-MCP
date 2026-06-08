from typing import List
from pydantic import BaseModel
from stock_manager_mcp.models.holding import Holding

class HoldingsResponse(BaseModel):
    holdings: List[Holding]