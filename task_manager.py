from models import Smith, HitResult
from validators import validate_power
from utils import wait_for_spacebar_press, duration_to_power

def perform_smith_hit(smith: Smith) -> HitResult:
    duration = wait_for_spacebar_press()
    raw_power = duration_to_power(duration, smith.max_power)
    power = validate_power(raw_power, smith.max_power)
    percentage = power / smith.max_power * 100

    if percentage < 30:
        desc = "Zwakke slag, de aambeeld lacht je uit."
    elif percentage < 70:
        desc = "Redelijke slag, de vonken vliegen."
    else:
        desc = "MONSTERHIT! De hele smidse trilt."

    return HitResult(power=power, percentage=percentage, description=desc)
