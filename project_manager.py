from models import Question

def load_questions():
    return [
        Question(
            question="Wat is de hoofdstad van Frankrijk?",
            options=["Berlijn", "Parijs", "Rome"],
            correct_answer=2
        ),
        Question(
            question="Wie schreef de theorie van evolutie?",
            options=["Newton", "Darwin", "Einstein"],
            correct_answer=2
        ),
        # Vul aan tot 10
    ]
