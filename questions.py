import random

def get_questions(skills):
    data = {
        "python": [
            "What is a list in Python?",
            "Explain OOP concepts",
            "What is a decorator?",
            "What is lambda function?",
            "Difference between list and tuple?"
        ],
        "sql": [
            "What is JOIN?",
            "Difference between WHERE and HAVING?",
            "What is normalization?",
            "What is primary key?",
            "Explain GROUP BY"
        ]
    }
    all_questions = []

    for skill in skills:
        all_questions.extend(data.get(skill.lower(), []))


    all_questions = data.get(skill.lower(), ["No questions available"])

    random.shuffle(all_questions)
    return all_questions[:3]  # random 5 questions