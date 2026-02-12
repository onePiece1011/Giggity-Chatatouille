from validators import valid_answer

def calculate_score(questions, form):
    score = 0
    for i, q in enumerate(questions):
        answer = form.get(f"q{i}")
        if valid_answer(answer, q.options) and answer == q.correct:
            score += 1
    return score
