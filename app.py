from flask import Flask, render_template, request
import os

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

    return f"Video uploaded: {video.filename}"

if __name__ == "__main__":
    app.run()
