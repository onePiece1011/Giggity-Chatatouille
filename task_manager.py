from validators import validate_answer

def ask_question(question):
    print(question.question)
    for idx, option in enumerate(question.options, start=1):
        print(f"{idx}. {option}")

    answer = input("Jouw antwoord (1-3): ")
    while not validate_answer(answer):
        answer = input("Ongeldig. Kies 1, 2 of 3: ")

    return int(answer) == question.correct_answer
