import whisper

# Load Whisper AI model
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]

# Example: Convert a recorded file to text
audio_file = "test_audio.wav"  # Replace with an actual file
print("Transcription:", transcribe_audio(audio_file))
