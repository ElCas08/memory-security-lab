import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)



from baseline import Baseline


baseline = Baseline()

baseline.record("credential", 4)
baseline.record("credential", 5)
baseline.record("credential", 4)
baseline.record("credential", 6)

print("Observed behavior:")
print(baseline.data)

print("\nAverage:")
print(baseline.average("credential"))

baseline.save()

print("\nBaseline saved.")