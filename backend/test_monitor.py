from memory_monitor import SensitiveDataMonitor


monitor = SensitiveDataMonitor()

monitor.register("api_key", "credential")
monitor.register("user_email", "personal_data")
monitor.register("password", "credential")

print("AFTER REGISTERING:")
print(monitor.report())


monitor.release("password")

print("\nAFTER RELEASING PASSWORD:")
print(monitor.report())


print("\nSTILL ACTIVE:")
print(monitor.active_items())