from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():

    result = {
        "name": "api_key",
        "category": "credential",
        "status": "ANOMALOUS RETENTION",
        "idle_time": 8.0,
        "normal_idle": 0.0,
        "risk": "HIGH"
    }

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
