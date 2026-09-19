import sys
import os
from datetime import datetime

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from flask import Flask, render_template, request
from security_engine import run_security_check
from security_analyst import SecurityAnalyst


app = Flask(__name__)

event_history = []
analyst = SecurityAnalyst()

def add_event(result):

    event_history.insert(
        0,
        {
            "time": datetime.now().strftime("%H:%M:%S"),
            "name": result["name"],
            "category": result["category"],
            "status": result["status"],
            "idle_time": result["idle_time"],
            "remediation": result["remediation"]
        }
    )

    # Keep the dashboard lightweight
    if len(event_history) > 12:
        event_history.pop()


@app.route("/")
def dashboard():

    result = run_security_check(
        anomalous=True
    )

    analysis = analyst.analyze(result)

    add_event(result)

    return render_template(
        "dashboard.html",
        result=result,
        analysis=analysis,
        events=event_history
    )

@app.route("/test", methods=["POST"])
def test():

    test_type = request.form.get("type")

    if test_type == "normal":

        result = run_security_check(
            anomalous=False
        )

    else:

        result = run_security_check(
            anomalous=True
        )

    analysis = analyst.analyze(result)

    add_event(result)

    return render_template(
        "dashboard.html",
        result=result,
        analysis=analysis,
        events=event_history
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )