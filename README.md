# Whisper Speech-to-Text API 🎤➡️📝

This is a simple API that converts **speech (audio)** into **text** using OpenAI’s pre-trained **Whisper model** (via `faster-whisper`).  
It is built with **FastAPI** and runs locally or on a server.

## 🚀 Features
- Accepts audio files (`.mp3`, `.wav`, `.m4a`, etc.).
- Auto language detection (works for English, Urdu, Hindi, Arabic, etc.).
- Returns transcription in JSON format.
- Easy to run with Python.


## 🛠️ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/whisper-api.git
cd whisper-api

### 2. Install dependencies
Make sure you have Python 3.9+ installed, then run:


pip install -r requirements.txt
Also install ffmpeg:

Windows: choco install ffmpeg

Linux (Debian/Ubuntu): sudo apt-get install ffmpeg

### 3. Run the API

python -m uvicorn main:app --reload
You should see:

Uvicorn running on http://127.0.0.1:8000
📌 Usage
Open your browser at 👉 http://127.0.0.1:8000/docs
(Swagger UI will appear).

Click on POST /transcribe → Try it out.

Upload an audio file and press Execute.

You’ll get a JSON response like:


{
  "language": "en",
  "text": "Hello, how are you?"
}

📦 API Endpoint
POST /transcribe
Input: audio file (.mp3, .wav, .m4a)

Output: JSON

{
  "language": "ur",
  "text": "آپ کیسے ہیں"
}
🔧 Configurations
In main.py you can change:


model = WhisperModel("small", device="cpu", compute_type="int8")
Models: tiny, base, small, medium, large-v3

Device: "cpu" or "cuda" (if GPU available)

Compute type: int8, float16, float32 (affects speed/accuracy)

👨‍💻 Author
Developed by Ahmed Ali during internship.
Uses OpenAI Whisper + FastAPI.

