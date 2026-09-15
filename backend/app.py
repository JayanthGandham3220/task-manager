from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Learn Jenkins"}
]

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json

    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"]
    }

    tasks.append(new_task)

    return jsonify(new_task)

@app.route("/")
def home():
    return "Task Manager Backend is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
