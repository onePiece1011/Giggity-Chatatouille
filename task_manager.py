from validators import is_valid_answer

def calculate_score(questions, form):
    score = 0
    for index, question in enumerate(questions):
        answer = form.get(f"q{index}")
        if answer and is_valid_answer(answer, question.options):
            if answer == question.correct:
                score += 1
    return score
