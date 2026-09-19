class AnomalyDetector:

    def __init__(self, baseline):
        self.baseline = baseline

    def deviation(self, category, current_duration):

        normal = self.baseline.average(category)

        if normal is None:
            return None

        if normal == 0:
            return 0

        return abs(current_duration - normal) / normal

    def classify(self, category, current_duration):

        deviation = self.deviation(
            category,
            current_duration
        )

        if deviation is None:
            return "NO_BASELINE"

        if deviation < 0.5:
            return "NORMAL"

        if deviation < 2:
            return "UNUSUAL"

        return "HIGHLY_UNUSUAL"