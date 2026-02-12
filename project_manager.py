from models import Smith
from task_manager import perform_smith_hit

class SmithGame:
    def __init__(self, smith_name: str = "Grom"):
        self.smith = Smith(name=smith_name)

    def run_round(self):
        result = perform_smith_hit(self.smith)
        print(f"\n{self.smith.name} slaat met kracht: {result.power}/"
              f"{self.smith.max_power} ({result.percentage:.1f}%)")
        print(result.description)

    def run(self):
        print("=== Smith Power Hit ===")
        while True:
            self.run_round()
            again = input("\nNog een slag? (j/n): ").strip().lower()
            if again != "j":
                print("Einde spel. Tot de volgende keer!")
                break
