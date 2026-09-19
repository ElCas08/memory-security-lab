import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from baseline import Baseline
from anomaly import AnomalyDetector


baseline = Baseline()
baseline.load()

detector = AnomalyDetector(baseline)


tests = [5, 10, 15, 30]

for duration in tests:

    result = detector.classify(
        "credential",
        duration
    )

    print(
        f"Duration: {duration}s "
        f"→ {result}"
    )