class AnomalyDetector:

    def __init__(self, baseline):
        self.baseline = baseline

    def idle_deviation(self, category, current_idle):

        normal = self.baseline.average_idle_time(category)

        if normal is None:
            return None

        # Normal behavior is approximately zero idle time.
        # In that case, any meaningful idle period is unusual.
        if normal < 0.001:

            if current_idle < 1:
                return 0

            return current_idle

        return abs(current_idle - normal) / normal

    def classify_idle(self, category, current_idle):

        deviation = self.idle_deviation(
            category,
            current_idle
        )

        if deviation is None:
            return "NO_BASELINE"

        if deviation < 0.5:
            return "NORMAL"

        if deviation < 2:
            return "UNUSUAL"

        return "HIGHLY_UNUSUAL"