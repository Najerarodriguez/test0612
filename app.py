# app.py
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Configura la conexión con Firebase
cred = credentials.Certificate("path/to/your/credentials.json")
firebase_admin.initialize_app(cred, {"projectId": "your-project-id"})
db = firestore.client()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
