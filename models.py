from dataclasses import dataclass

@dataclass
class Question:
    question: str
    options: list
    correct_answer: int
