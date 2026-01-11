from flask import Flask, render_template, request, jsonify
from ai_engine import run_ai
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "audio" not in request.files:
        return jsonify({"error": "No audio uploaded"})

    audio = request.files["audio"]
    path = "audio.wav"
    audio.save(path)

    result = run_ai(path)

    os.remove(path)

    return jsonify(result)

if __name__ == "__main__":
    app.run()
