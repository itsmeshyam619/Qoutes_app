
from flask import Flask, jsonify, request, render_template
import random
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

qoutes = [
    {"id": 1, "text": "The only way to do great work is to love what you do. — Steve Jobs"},
    {"id": 2, "text": "Success is not the key to happiness. Happiness is the key to success. — Albert Schweitzer"},
    {"id": 3, "text": "DevOps is not a goal, but a never-ending process of continual improvement. — Jez Humble"},
    {"id": 4, "text": "It always seems impossible until it’s done. — Nelson Mandela"},
    {"id": 5, "text": "Do not wait to strike till the iron is hot; but make it hot by striking. — William Butler Yeats"},
    {"id": 6, "text": "The best way to predict the future is to invent it. — Alan Kay"},
    {"id": 7, "text": "If you want to lift yourself up, lift up someone else. — Booker T. Washington"},
    {"id": 8, "text": "Quality means doing it right when no one is looking. — Henry Ford"},
    {"id": 9, "text": "Simplicity is the soul of efficiency. — Austin Freeman"},
    {"id": 10, "text": "The secret of getting ahead is getting started. — Mark Twain"},
    {"id": 11, "text": "Innovation distinguishes between a leader and a follower. — Steve Jobs"},
    {"id": 12, "text": "The only limit to our realization of tomorrow will be our doubts of today. — Franklin D. Roosevelt"},
    {"id": 13, "text": "If you can dream it, you can do it. — Walt Disney"},
    {"id": 14, "text": "The way to get started is to quit talking and begin doing. — Walt Disney"},
    {"id": 15, "text": "Don’t watch the clock; do what it does. Keep going. — Sam Levenson"},
    {"id": 16, "text": "Perfection is not attainable, but if we chase perfection we can catch excellence. — Vince Lombardi"},
    {"id": 17, "text": "Success is walking from failure to failure with no loss of enthusiasm. — Winston Churchill"},
    {"id": 18, "text": "The only source of knowledge is experience. — Albert Einstein"},
    {"id": 19, "text": "Strive not to be a success, but rather to be of value. — Albert Einstein"},
    {"id": 20, "text": "The greatest glory in living lies not in never falling, but in rising every time we fall. — Nelson Mandela"},
    {"id": 21, "text": "Opportunities don't happen. You create them. — Chris Grosser"},
    {"id": 22, "text": "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill"},
    {"id": 23, "text": "Don’t be afraid to give up the good to go for the great. — John D. Rockefeller"},
    {"id": 24, "text": "I have not failed. I've just found 10,000 ways that won't work. — Thomas Edison"},
    {"id": 25, "text": "The only thing worse than starting something and failing is not starting something. — Seth Godin"},
    {"id": 26, "text": "If you really look closely, most overnight successes took a long time. — Steve Jobs"},
    {"id": 27, "text": "Success is the sum of small efforts, repeated day in and day out. — Robert Collier"},
    {"id": 28, "text": "Don’t let yesterday take up too much of today. — Will Rogers"},
    {"id": 29, "text": "The future depends on what you do today. — Mahatma Gandhi"},
    {"id": 30, "text": "The harder you work for something, the greater you’ll feel when you achieve it. — Unknown"},
    {"id": 31, "text": "Dream bigger. Do bigger. — Unknown"},
    {"id": 32, "text": "Push yourself, because no one else is going to do it for you. — Unknown"},
    {"id": 33, "text": "Great things never come from comfort zones. — Neil Strauss"}
]

@app.route("/")
def home():
    return render_template("index.html")

# Get all qoutes
@app.route("/jokes", methods=["GET"])
def get_all_qoutes():
    return jsonify(qoutes), 200

# Get a random qoute
@app.route("/jokes/random", methods=["GET"])
def get_random_qoute():
    if not qoutes:
        return jsonify({"error": "No qoutes available"}), 404
    return jsonify(random.choice(qoutes)), 200

# Get qoute by id
@app.route("/jokes/<int:qoute_id>", methods=["GET"])
def get_qoute_by_id(qoute_id):
    qoute = next((j for j in qoutes if j["id"] == qoute_id), None)
    if qoute:
        return jsonify(qoute), 200
    return jsonify({"error": "Qoute not found"}), 404

# Add a new qoute
@app.route("/jokes", methods=["POST"])
def add_qoute():
    data = request.get_json()
    if not data or "text" not in data or len(data["text"].strip()) < 3:
        return jsonify({"error": "Qoute must be at least 3 characters."}), 400
    new_id = max((j["id"] for j in qoutes), default=0) + 1
    new_qoute = {"id": new_id, "text": data["text"].strip()}
    qoutes.append(new_qoute)
    return jsonify(new_qoute), 201

# Update a qoute
@app.route("/jokes/<int:qoute_id>", methods=["PUT"])
def update_qoute(qoute_id):
    data = request.get_json()
    if not data or "text" not in data or len(data["text"].strip()) < 3:
        return jsonify({"error": "Qoute must be at least 3 characters."}), 400
    for qoute in qoutes:
        if qoute["id"] == qoute_id:
            qoute["text"] = data["text"].strip()
            return jsonify(qoute), 200
    return jsonify({"error": "Qoute not found"}), 404

# Delete a qoute
@app.route("/jokes/<int:qoute_id>", methods=["DELETE"])
def delete_qoute(qoute_id):
    global qoutes
    if not any(j["id"] == qoute_id for j in qoutes):
        return jsonify({"error": "Qoute not found"}), 404
    qoutes = [j for j in qoutes if j["id"] != qoute_id]
    return jsonify({"message": f"Qoute {qoute_id} deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
