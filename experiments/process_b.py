import os
import time

secret = "PROGRAM B'S SECRET"

print("Program B")
print("PID:", os.getpid())
print("Secret:", secret)

print("\nProgram B is running...")
print("Press Ctrl+C to stop.")

while True:
    time.sleep(1)