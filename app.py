from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Famous' first Flask API!"

# Greet route
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify({
        "message": f"Hello, {name}! Welcome to your first deployed Python API."
    })

# Current time route
@app.route('/time')
def get_time():
    now = datetime.now()
    return jsonify({
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S")
    })

# Motivational quote route
@app.route('/quote')
def get_quote():
    quotes = [
        "Keep going, you’re doing great!",
        "Every expert was once a beginner.",
        "Success is built on persistence, not luck.",
        "Dream big, code bigger!",
        "Progress, not perfection.",
        "A curious mind is a fertile land for growth"
    ]
    return jsonify({
        "quote": random.choice(quotes)
    })

# Simple calculator route
@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({
            "result": a + b
        })
    except ValueError:
        return jsonify({"error": "Invalid numbers supplied."}), 400


if __name__ == '__main__':
    app.run(debug=True)


