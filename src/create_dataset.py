import json


class CreateDataset:
    def __init__(self):
        self.json_path = 'data.json'
        self.csv_path = '../paris-2024-faq.csv'
        with open(self.json_path) as file:
            self.dataset = json.load(file)
        f = open(self.csv_path, 'r')
        dataset_split = f.read().split(";")
        question = False
        for data in dataset_split:
            if question:
                question = False
                self.dataset["intents"][-1]["responses"].append(data)

            if "?" in data:
                question = True
                self.dataset["intents"].append({
                    "tag": "",
                    "patterns": [
                        data
                    ],
                    "responses": [
                    ]
                })
        with open(self.json_path, 'w') as f:
            json.dump(self.dataset, f)


CreateDataset()
