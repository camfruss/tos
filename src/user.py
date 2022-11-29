from position import Position
from __future__ import annotations

class User:

    taxes = 0
    profit = 0
    cash = 0
    margin = 0
    positions: list[Position] = []

    def __init__(self):
        pass
        # need to load positions
