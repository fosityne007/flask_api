# 🌐 Famous' Flask API

A simple and beginner-friendly **Flask REST API** built and deployed by **Osiaro Famous**.  
This project demonstrates how to create, test, and deploy Python Flask applications online using **PythonAnywhere**.

---

## 🚀 Live API
**Base URL:** [https://fosityne.pythonanywhere.com](https://fosityne.pythonanywhere.com)

You can test the endpoints directly in your browser or with tools like **Postman** or **Thunder Client**.

---

## 📍 API Endpoints

### 1. Home
**GET** `/`  
Returns a welcome message.

**Example Response:**
```json
{
  "message": "Welcome to Famous’ first Flask API!"
}

4. Motivational Quote

GET /quote
Returns a random motivational quote, including one by Famous himself.

Example Response:

{
  "quote": "A curious mind is a fertile land for growth."
}

5. Add Numbers

GET /add?a=5&b=10
Performs simple addition between two numbers.

Example Response:

{
  "result": 15
}

🧠 Motivation

“A curious mind is a fertile land for growth.” — Osiaro Famous

This project was created to strengthen my understanding of backend development, RESTful API design, and web deployment using Flask and PythonAnywhere.

⚙️ Tech Stack

Python 3

Flask

Postman / Thunder Client for testing

PythonAnywhere for deployment

💻 Running Locally
# Clone the repository
git clone https://github.com/fosityne007/flask_api.git

# Navigate into the project
cd flask_api

# Install dependencies
pip install flask

# Run the app
python app.py


The app is live at http://127.0.0.1:5000

📦 Deployment

The live version is deployed via PythonAnywhere, configured using a WSGI file.

👤 Author

Osiaro Famous .O
Backend Developer | Flask Enthusiast
📫 GitHub: fosityne007