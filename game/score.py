import datetime as dtm
import json


class ScoreManager:
    def create_result(self, name, rounds, score):
        data = dtm.datetime.now()
        result = {
        "Date": str(data),
        "Name": name,
        "Number of rounds": rounds,
        "Final score": score
        }
        return result


    def read_results(self):
        with open("results.json", "r", encoding="UTF-8") as file:
            results = json.load(file)
        return results

    
    def write_results(self, results):
        with open("results.json", "w", encoding="UTF-8") as file:
            json.dump(results, file, indent=4)


    def save_result(self, name, rounds, score):
        result = self.create_result(name, rounds, score)
        results = self.read_results()
        results.append(result)
        self.write_results(results)
    

    def get_results(self):
        results = self.read_results()
        for res in results:
            print(f"Date: {res['Date']}")
            print(f"Name: {res['Name']}")
            print(f"Number of rounds: {res['Number of rounds']}")
            print(f"Final score: {res['Final score']}")
            print("-"*32)


