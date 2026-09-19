import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from flask import Flask, render_template, request
from security_engine import run_security_check


app = Flask(__name__)


@app.route("/")
def dashboard():

    # Default: show anomaly result
    result = run_security_check(
        anomalous=True
    )

    return render_template(
        "dashboard.html",
        result=result
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

    return render_template(
        "dashboard.html",
        result=result
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
