# app.py
from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Configura la conexión con Firebase
cred = credentials.Certificate("C:\\Users\\root\\Documents\\KAYI\\kayicash20231206\\test20231206-87d2d-firebase-adminsdk-1b922-8b9e62a351.json")
firebase_admin.initialize_app(cred, {"projectId": "test20231206-87d2d"})
db = firestore.client()

@app.route("/")
def index():
    return render_template("index.html")

# app.py (continuación)
@app.route("/guardar", methods=["POST"])
def guardar():
    numero = float(request.form.get("numero"))

    # Guarda el número en la base de datos Firebase
    #doc_ref = db.collection("numeros").add({"numero": numero})

    #return f"Número {numero} guardado con éxito con ID: {doc_ref.id}"
    doc_ref, doc_id = db.collection("numeros").add({"numero": numero})
    return f"Número {numero} guardado con éxito con ID: {doc_id}"



if __name__ == "__main__":
    app.run(debug=True)
