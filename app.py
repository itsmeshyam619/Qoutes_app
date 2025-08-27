from flask import Flask, jsonify
import random
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

jokes = [
    "Why do Python developers wear glasses? Because they can't C!",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Debugging: Removing the needles from the haystack."
]

@app.route("/joke")
def get_joke():
    return jsonify({"joke": random.choice(jokes)})

@app.route("/")
def home():
    return "Welcome to Jokes API! Visit /joke for a random joke."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
