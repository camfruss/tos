
class Option:
    
    ticker: str
    strike: float
    cost: float
    quantity: int  # 0 if not held / part of option chain
