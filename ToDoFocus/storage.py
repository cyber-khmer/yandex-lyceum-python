import json


def load_data():
    try:
        with open('tasks.json', 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        return None

def save_data(data):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
