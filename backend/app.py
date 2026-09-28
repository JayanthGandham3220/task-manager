from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")

# Database
db = client["taskdb"]

# Collection
tasks_collection = db["tasks"]


@app.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = list(tasks_collection.find({}, {"_id": 0}))

    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():

    data = request.json

    new_task = {
        "id": tasks_collection.count_documents({}) + 1,
        "task": data["task"]
    }

    tasks_collection.insert_one(new_task)

    return jsonify(new_task)


@app.route("/")
def home():
    return "Task Manager Backend is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
