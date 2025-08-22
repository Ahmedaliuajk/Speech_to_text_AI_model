from fastapi import FastAPI, UploadFile, File
from faster_whisper import WhisperModel
import uvicorn
import tempfile

# Load pre-trained whisper model
# Options: tiny, base, small, medium, large-v3
model = WhisperModel("small", device="cpu", compute_type="int8")

app = FastAPI(title="Whisper Speech-to-Text API")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Transcribe
    segments, info = model.transcribe(tmp_path)
    text = " ".join([seg.text for seg in segments])

    return {"language": info.language, "text": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)