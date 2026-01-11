import whisper
import cv2
from textblob import TextBlob

model = whisper.load_model("base")

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

def analyze_language(text):
    blob = TextBlob(text)

    words = len(text.split())
    confidence = min(words / 25, 10)

    fluency = 10 - text.lower().count("um") - text.lower().count("uh")
    fluency = max(fluency, 1)

    clarity = len(blob.sentences)

    return {
        "confidence": round(confidence, 2),
        "fluency": round(fluency, 2),
        "clarity": clarity,
        "text": text
    }

def analyze_eye_contact():
    # Render Free cannot process video, so simulate for now
    return 7.5

def run_ai(audio_path):
    text = transcribe(audio_path)
    lang = analyze_language(text)
    eyes = analyze_eye_contact()

    overall = round((lang["confidence"] + eyes) / 2, 2)

    return {
        "speech": lang,
        "eye_contact": eyes,
        "overall_score": overall
    }
