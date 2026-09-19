import sys
import os
import time

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from baseline import Baseline
from memory_monitor import SensitiveDataMonitor


baseline = Baseline()
baseline.load()

monitor = SensitiveDataMonitor()


print("MONITORING MODE")
print("----------------")

monitor.register(
    "api_key",
    "credential"
)

print("API key registered.")

monitor.access("api_key")

print("API key accessed.")

print("\nApplication has finished using the API key.")
print("But the API key is NOT released.")

print("\nWaiting 8 seconds...")

time.sleep(8)


item = monitor.report()[0]

idle_time = (
    time.time()
    - item["last_accessed"].timestamp()
)

normal_idle = baseline.average_idle_time(
    "credential"
)


print("\nSECURITY RESULT")
print("----------------")

print(
    f"Observed idle time: "
    f"{idle_time:.2f}s"
)

print(
    f"Normal idle time: "
    f"{normal_idle:.4f}s"
)


if idle_time > normal_idle + 3:

    print(
        "\n⚠ UNUSUAL SENSITIVE-DATA RETENTION"
    )

    print(
        "The credential remains active "
        "after its last observed use."
    )

else:

    print(
        "\n✓ Behavior is within the learned baseline."
    )