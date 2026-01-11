import moviepy.editor as mp

def extract_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path)
    return audio_path
