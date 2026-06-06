import datetime as dtm
import json

def save_result(name, rounds, score):
    data = dtm.datetime.now()
    result = {
        "Date": str(data),
        "Name": name,
        "Number of rounds": rounds,
        "Final score": score
    }
    with open("results.json", "r", encoding="UTF-8") as file:
        results = json.load(file)
        results.append(result)
    with open("results.json", "w", encoding="UTF-8") as file:
        json.dump(results, file, indent=4)
        



# def get_results():
