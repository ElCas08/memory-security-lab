class SecurityAnalyst:

    def analyze(self, result):

        status = result.get("status")
        name = result.get("name")
        category = result.get("category")

        idle_time = result.get("idle_time", 0)
        normal_idle = result.get("normal_idle", 0)

        remediation = result.get("remediation")

        # =========================================
        # NORMAL EVENT
        # =========================================

        if status == "NORMAL":

            return {
                "summary":
                    f"{name} behaved within its learned "
                    f"{category} lifecycle.",

                "why_flagged":
                    "No abnormal retention was detected. "
                    "The observed lifecycle remained consistent "
                    "with the learned behavioral baseline.",

                "action":
                    "No remediation required.",

                "verification":
                    "Credential lifecycle completed normally.",

                "assessment":
                    "The security engine observed normal behavior "
                    "and did not identify a retention anomaly.",

                "next_step":
                    "No action is required. Continue normal "
                    "application operation and monitoring.",

                "evidence": {
                    "observed": f"{idle_time}s",
                    "baseline": f"{normal_idle}s",
                    "deviation": "NONE",
                    "result": "NORMAL"
                }
            }

        # =========================================
        # ANOMALOUS EVENT
        # =========================================

        if remediation:

            action = (
                f"{remediation.get('action', 'REMEDIATION')} "
                f"was applied to "
                f"{remediation.get('target', name)}."
            )

            verification = (
                "The credential was released and marked inactive. "
                "Remediation completed successfully."
            )

            result_state = "MITIGATED"

        else:

            action = (
                "The event was detected, but no remediation "
                "was executed."
            )

            verification = (
                "The security engine is continuing to monitor "
                "the sensitive data."
            )

            result_state = "MONITORING"

        return {
            "summary":
                f"Vigilio detected abnormal "
                f"{category} retention.",

            "why_flagged":
                f"{name} remained active for {idle_time} seconds "
                f"after its last observed use, while the learned "
                f"normal idle time is {normal_idle} seconds.",

            "action":
                action,

            "verification":
                verification,

            "assessment":
                f"The behavioral engine classified this event as "
                f"{status}. The observed lifecycle deviated "
                f"substantially from the learned baseline.",

            "next_step":
                "Review the affected credential and confirm that "
                "the application no longer requires it. If the "
                "credential is still needed, allow the application "
                "to reacquire it through its normal secure flow.",

            "evidence": {
                "observed": f"{idle_time}s",
                "baseline": f"{normal_idle}s",
                "deviation": status,
                "result": result_state
            }
        }