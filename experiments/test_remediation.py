from memory_monitor import SensitiveDataMonitor
from remediation import RemediationEngine


monitor = SensitiveDataMonitor()

monitor.register(
    "api_key",
    "credential"
)

monitor.access("api_key")

print("\nBEFORE REMEDIATION")
print("------------------")

print(
    monitor.report()
)


remediation = RemediationEngine(
    monitor
)

action = remediation.release_sensitive_data(
    "api_key"
)


print("\nREMEDIATION")
print("-----------")

print(
    action
)


print("\nAFTER REMEDIATION")
print("-----------------")

print(
    monitor.report()
)
