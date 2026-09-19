import time

from baseline import Baseline
from memory_monitor import SensitiveDataMonitor
from anomaly import AnomalyDetector


def run_security_check(anomalous=True):

    # Load learned normal behavior
    baseline = Baseline()
    baseline.load()

    # Create security monitor
    monitor = SensitiveDataMonitor()

    # Create anomaly detector
    detector = AnomalyDetector(baseline)

    # Track sensitive data
    monitor.register(
        "api_key",
        "credential"
    )

    # Application uses the API key
    monitor.access("api_key")

    if anomalous:

        # Simulate suspicious retention
        time.sleep(8)

    else:

        # Normal behavior:
        # release immediately after use
        monitor.release("api_key")

    # Get current information
    item = monitor.report()[0]

    # Calculate idle time
    if item["last_accessed"] is not None:

        idle_time = (
            time.time()
            - item["last_accessed"].timestamp()
        )

    else:

        idle_time = 0

    # Detect behavior
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

    print("\nNORMAL TEST")
    print("-----------")

    result = run_security_check(
        anomalous=False
    )

    for key, value in result.items():
        print(f"{key}: {value}")


    print("\nANOMALY TEST")
    print("------------")

    result = run_security_check(
        anomalous=True
    )

    for key, value in result.items():
        print(f"{key}: {value}")
