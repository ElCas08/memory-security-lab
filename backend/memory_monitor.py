from datetime import datetime


class SensitiveDataMonitor:

    def __init__(self):
        self.items = []

        # Temporary experiment thresholds
        self.thresholds = {
            "credential": 3,
            "personal_data": 10
        }

    def register(self, name, category):
        item = {
            "name": name,
            "category": category,
            "created_at": datetime.now(),
            "released_at": None,
            "last_accessed": None,
            "access_count": 0,
            "active": True
        }

        self.items.append(item)

    def access(self, name):
        for item in self.items:
            if item["name"] == name and item["active"]:
                item["last_accessed"] = datetime.now()
                item["access_count"] += 1

    def release(self, name):
        for item in self.items:
            if item["name"] == name and item["active"]:
                item["active"] = False
                item["released_at"] = datetime.now()

    def report(self):
        return self.items

    def active_items(self):
        return [
            item
            for item in self.items
            if item["active"]
        ]

    def exposure_duration(self, item):
        if item["released_at"] is not None:
            end_time = item["released_at"]
        else:
            end_time = datetime.now()

        return (
            end_time - item["created_at"]
        ).total_seconds()

    def time_since_last_access(self, item):
        if item["last_accessed"] is None:
            return None

        return (
            datetime.now() - item["last_accessed"]
        ).total_seconds()

    def check_risk(self, item):

        # Released data is not currently exposed
        if not item["active"]:
            return "OK"

        # Has the data ever actually been used?
        if item["access_count"] == 0:
            return "UNUSED"

        idle_time = self.time_since_last_access(item)

        if idle_time is not None and idle_time > 3:
            return "IDLE"

        return "OK"

    def security_report(self):

        active = self.active_items()

        report = {
            "total_tracked": len(self.items),
            "active": len(active),
            "released": len(self.items) - len(active),
            "alerts": []
        }

        for item in self.items:

            duration = self.exposure_duration(item)
            risk = self.check_risk(item)

            report["alerts"].append({
                "name": item["name"],
                "category": item["category"],
                "active": item["active"],
                "duration_seconds": round(duration, 2),
                "access_count": item["access_count"],
                "last_accessed": item["last_accessed"],
                "risk": risk
            })

        return report