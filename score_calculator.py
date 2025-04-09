# score_calculator.py
import json

def average_score():
    with open("feedback_data.json") as f:
        data = json.load(f)
    
    total = sum(item["score"] for item in data)
    print(f"Average Score: {total / len(data):.2f}")

average_score()
