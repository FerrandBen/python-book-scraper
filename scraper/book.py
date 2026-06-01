from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    price: float
    score: int
    availability : bool