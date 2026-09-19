from datetime import datetime


class RemediationEngine:

    def __init__(self, monitor):
        self.monitor = monitor
        self.actions = []

    def release_sensitive_data(self, name):
        """
        Release sensitive data after an anomaly is detected.
        """

        self.monitor.release(name)

        action = {
            "action": "RELEASE",
            "target": name,
            "timestamp": datetime.now(),
            "status": "MITIGATED"
        }

        self.actions.append(action)

        return action

    def history(self):
        """
        Return remediation actions taken.
        """

        return self.actions

