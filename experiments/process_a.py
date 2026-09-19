import os
import time
import sys

# Allow Python to find our backend module
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from memory_monitor import SensitiveDataMonitor


monitor = SensitiveDataMonitor()


# Sensitive data used by our test application
username = "alice@example.com"
api_key = "TEST_API_KEY_123456"
password = "TEST_PASSWORD_123"


# Register the data with our security monitor
monitor.register("username", "personal_data")
monitor.register("api_key", "credential")
monitor.register("password", "credential")


print("Test application running")
print("PID:", os.getpid())

print("\nInitial sensitive data:")

for item in monitor.active_items():
    print(
        f"- {item['name']} "
        f"({item['category']})"
    )


# Simulate the application using the password
print("\nApplication is using the password...")

monitor.access("password")

time.sleep(2)

monitor.access("password")

time.sleep(3)


print("\nApplication is using the API key...")

monitor.access("api_key")

print("API key used once.")

time.sleep(5)


# Application is finished with the password
print("\nReleasing password...")

password = None
monitor.release("password")


print("\nCurrent sensitive data:")

for item in monitor.report():
    status = "ACTIVE" if item["active"] else "RELEASED"

    print(
        f"- {item['name']} "
        f"({item['category']}) "
        f"→ {status}"
    )

print("\nSECURITY REPORT")

report = monitor.security_report()

print(f"Total tracked: {report['total_tracked']}")
print(f"Active: {report['active']}")
print(f"Released: {report['released']}")

for item in report["alerts"]:

    status = "ACTIVE" if item["active"] else "RELEASED"

    print(
    f"- {item['name']} "
    f"({item['category']}) "
    f"→ {status} "
    f"| accesses: {item['access_count']} "
    f"| duration: {item['duration_seconds']} seconds "
    f"| risk: {item['risk']}"
    )

print("\nApplication continues running...")


while True:
    time.sleep(1)