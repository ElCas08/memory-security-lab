import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "backend")
    )
)

from flask import Flask, render_template
from security_engine import run_security_check


app = Flask(__name__)


@app.route("/")
def dashboard():

    result = run_security_check()

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
