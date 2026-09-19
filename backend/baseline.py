import json
import os


class Baseline:

    def __init__(self, filename="baseline.json"):
        self.filename = filename
        self.data = {}

    def record(self, category, lifetime, idle_time):
        if category not in self.data:
            self.data[category] = {
                "lifetimes": [],
                "idle_times": []
            }

        self.data[category]["lifetimes"].append(lifetime)
        self.data[category]["idle_times"].append(idle_time)

    def average_lifetime(self, category):
        values = self.data.get(category, {}).get(
            "lifetimes", []
        )

        if not values:
            return None

        return sum(values) / len(values)

    def average_idle_time(self, category):
        values = self.data.get(category, {}).get(
            "idle_times", []
        )

        if not values:
            return None

        return sum(values) / len(values)

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=2)

    def load(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            self.data = json.load(file)