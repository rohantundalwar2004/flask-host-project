import moviepy.editor as mp
import whisper
import cv2
from textblob import TextBlob

# Load Whisper model once
model = whisper.load_model("base")

def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path)
    return audio_path

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

def analyze_language(text):
    blob = TextBlob(text)

    confidence = min(len(text.split()) / 30, 10)
    fluency = max(10 - text.lower().count("um") - text.lower().count("uh"), 1)
    clarity = len(blob.sentences)

    return {
        "confidence": round(confidence, 2),
        "fluency": round(fluency, 2),
        "clarity": clarity
    }

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    eye_frames = 0
    total = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        total += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if gray.mean() > 50:
            eye_frames += 1

    if total == 0:
        return 0

    return round((eye_frames / total) * 10, 2)

def run_ai(video_path):
    audio = extract_audio(video_path)
    text = transcribe(audio)
    speech = analyze_language(text)
    eye = analyze_video(video_path)

    overall = round((speech["confidence"] + eye) / 2, 2)

    return {
        "text": text,
        "speech": speech,
        "eye_contact": eye,
        "overall": overall
    }
