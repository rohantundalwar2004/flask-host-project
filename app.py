from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if "video" not in request.files:
        return "No video file found"

    video = request.files["video"]

    if video.filename == "":
        return "No video selected"

    save_path = os.path.join(app.config["UPLOAD_FOLDER"], video.filename)
    video.save(save_path)

    feedback = """
✔ Good confidence
✔ Voice clarity is decent
✖ Maintain more eye contact
✖ Improve body posture
✔ Slides are well structured
"""

    return render_template("result.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)