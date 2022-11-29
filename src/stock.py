from option import Option
from __future__ import annotations

class Stock:
    
    ticker: str
    quantity: int # 0 if not held
    option_chain: list[Option]
