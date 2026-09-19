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

print("LEARNING MODE")
print("-------------")

for run in range(3):

    monitor = SensitiveDataMonitor()

    monitor.register(
        "api_key",
        "credential"
    )

    print(f"\nRun {run + 1}")

    # Application uses the credential
    monitor.access("api_key")

    # Application releases it normally
    monitor.release("api_key")

    item = monitor.report()[0]

    lifetime = monitor.exposure_duration(item)

    # How long the data existed between last use and release
    idle_time = (
        item["released_at"]
        - item["last_accessed"]
    ).total_seconds()

    print(
        f"Lifetime: {lifetime:.2f}s"
    )

    print(
        f"Idle before release: {idle_time:.2f}s"
    )

    baseline.record(
        "credential",
        lifetime,
        idle_time
    )


baseline.save()

print("\nBASELINE")
print("--------")

print(
    "Average lifetime:",
    baseline.average_lifetime("credential")
)

print(
    "Average idle time:",
    baseline.average_idle_time("credential")
)