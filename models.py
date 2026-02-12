from dataclasses import dataclass

@dataclass
class Smith:
    name: str
    max_power: int = 100

@dataclass
class HitResult:
    power: int
    percentage: float
    description: str
