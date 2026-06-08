import pandas as pd

def evaluate_response(scores):
    """
    scores: dict with keys:
    accuracy, logic, adherence, completeness, safety
    """
    total = sum(scores.values())
    average = total / len(scores)
    return round(average, 2)

# Example
sample = {
    "accuracy": 4,
    "logic": 5,
    "adherence": 4,
    "completeness": 4,
    "safety": 5
}

print("Evaluation Score:", evaluate_response(sample))
