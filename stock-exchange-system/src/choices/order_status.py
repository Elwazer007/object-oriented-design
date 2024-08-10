from enum import Enum


class OrderStatus(Enum):
    PENDING = 1
    FILLED = 2
    CANCELLED = 3
    REJECTED = 4
    PARTIALLY_FILLED = 5
