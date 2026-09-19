import time

from baseline import Baseline
from memory_monitor import SensitiveDataMonitor
from anomaly import AnomalyDetector


def run_security_check():

    # Load what the application normally does
    baseline = Baseline()
    baseline.load()

    # Create our security monitor
    monitor = SensitiveDataMonitor()

    # Create detector using the learned baseline
    detector = AnomalyDetector(baseline)

    # Track sensitive data
    monitor.register(
        "api_key",
        "credential"
    )

    # Simulate the application using it
    monitor.access("api_key")

    # Simulate suspicious retention
    time.sleep(8)

    # Get information about the tracked data
    item = monitor.report()[0]

    # Calculate how long it has been idle
    idle_time = (
        time.time()
        - item["last_accessed"].timestamp()
    )

    # Ask our detector what it thinks
    status = detector.classify_idle(
        "credential",
        idle_time
    )

    normal_idle = baseline.average_idle_time(
        "credential"
    )

    return {
        "name": "api_key",
        "category": "credential",
        "idle_time": round(idle_time, 2),
        "normal_idle": round(normal_idle, 4),
        "status": status
    }

if __name__ == "__main__":

    result = run_security_check()

    print("\nSECURITY ENGINE RESULT")
    print("----------------------")

    for key, value in result.items():
        print(f"{key}: {value}")