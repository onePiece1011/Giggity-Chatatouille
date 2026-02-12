import time
import sys

def wait_for_spacebar_press(prompt: str = "Druk op spatie en houd vast..."):
    print(prompt)
    input("Druk op Enter om te beginnen met 'vasthouden' simuleren...")
    start = time.time()
    input("Laat Enter los om te stoppen (simuleert loslaten van spatie)...")
    end = time.time()
    duration = end - start
    return duration

def duration_to_power(duration: float, max_power: int = 100, max_seconds: float = 3.0) -> int:
    ratio = min(duration / max_seconds, 1.0)
    return int(ratio * max_power)
