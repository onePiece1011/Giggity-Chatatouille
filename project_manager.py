from flask import render_template, request
from models import Question
from task_manager import calculate_score
from utils import get_result

def load_questions():
    return [
        Question(
            "Wat is de hoofdstad van Frankrijk?",
            ["Berlijn", "Parijs", "Rome"],
            "Parijs"
        ),
        Question(
            "Wie ontwikkelde de evolutietheorie?",
            ["Darwin", "Newton", "Tesla"],
            "Darwin"
        ),
        # maak dit 10
    ]

def setup_routes(app):
    questions = load_questions()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/quiz", methods=["GET", "POST"])
    def quiz():
        if request.method == "POST":
            score = calculate_score(questions, request.form)
            result = get_result(score)
            return render_template("result.html", score=score, result=result)

        return render_template("quiz.html", questions=questions)
