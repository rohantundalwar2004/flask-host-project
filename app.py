from flask import Flask, render_template, request
import os
from ai_engine import run_ai

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    video = request.files["video"]
    path = os.path.join(app.config["UPLOAD_FOLDER"], video.filename)
    video.save(path)

    result = run_ai(path)

    return render_template("result.html", data=result)

