from flask import render_template, request
from models import Question
from task_manager import calculate_score
from utils import calculate_result

def load_questions():
    return [
        Question(
            "Wat is de hoofdstad van Frankrijk?",
            ["Berlijn", "Parijs", "Rome"],
            "Parijs"
        ),
        Question(
            "Wie ontwikkelde de evolutietheorie?",
            ["Newton", "Darwin", "Tesla"],
            "Darwin"
        ),
        Question(
            "Welke planeet is de grootste?",
            ["Mars", "Jupiter", "Venus"],
            "Jupiter"
        )
    ]

def register_routes(app):
    questions = load_questions()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/quiz", methods=["GET", "POST"])
    def quiz():
        if request.method == "POST":
            score = calculate_score(questions, request.form)
            result = calculate_result(score)
            return render_template("result.html", score=score, result=result)

        return render_template("quiz.html", questions=questions)
