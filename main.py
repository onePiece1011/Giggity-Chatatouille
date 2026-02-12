from project_manager import load_questions
from task_manager import ask_question
from utils import calculate_result

def start_game():
    print("=== QUIZ GAME START ===")
    questions = load_questions()
    score = 0

    for q in questions:
        if ask_question(q):
            score += 1

    result = calculate_result(score)
    print(f"\nScore: {score}/10")
    print(f"Resultaat: {result}")

if __name__ == "__main__":
    start_game()
