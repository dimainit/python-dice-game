import datetime as dtm
import json

def save_result(name, rounds, score):
    """Saves the final game result to results.json."""
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

def get_results():
    """Reads saved game results from results.json and prints them."""
    with open("results.json", "r", encoding="UTF-8") as file:
        results = json.load(file)
        for i in results:
           print(f"Date: {i['Date']}")
           print(f"Name: {i['Name']}")
           print(f"Number of rounds: {i['Number of rounds']}")
           print(f"Final score: {i['Final score']}")
           print("---------------------------------")