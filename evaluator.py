def evaluate_answer(answer):
    words = len(answer.split())  # simple logic

    if words > 25:
        return "Excellent Answer ✅", 90
    elif words > 15:
        return "Good Answer 👍", 70
    elif words > 8:
        return "Average Answer ⚠", 50
    else:
        return "Poor Answer ❌", 30
    
def evaluate_answer(answer):
    keywords = ["python", "data", "object", "function", "query"]

    score = 0
    for word in keywords:
        if word in answer.lower():
            score += 20

    if score >= 80:
        return "Excellent ✅", score
    elif score >= 50:
        return "Good 👍", score
    else:
        return "Improve ⚠", score