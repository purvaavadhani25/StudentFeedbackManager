# feedback_entry.py
import json

def collect_feedback():
    feedback = {
        "name": input("Student Name: "),
        "subject": input("Subject: "),
        "score": float(input("Score: ")),
        "comments": input("Comments: ")
    }
    try:
        with open("feedback_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    
    data.append(feedback)

    with open("feedback_data.json", "w") as f:
        json.dump(data, f, indent=4)

collect_feedback()
