def validate_power(power: int, max_power: int = 100) -> int:
    if power < 0:
        return 0
    if power > max_power:
        return max_power
    return power
