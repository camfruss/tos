from option import Option
from stock import Stock
from __future__ import annotations

class Position:
    
    stock: Stock 
    options: list[Option]

    def __init__(self):
        pass
    