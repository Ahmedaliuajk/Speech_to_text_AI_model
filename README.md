## Whisper Speech-to-Text API

This project provides a REST API for converting speech (audio files) into text using OpenAI’s Whisper model.
It is built with FastAPI and can be integrated into apps (e.g., WhatsApp clone, mobile apps, or web apps).

🚀 Features

Uses pre-trained Whisper model (small, medium, or large).

Accepts .mp3, .wav, .m4a audio formats.

Returns JSON output with detected language and transcribed text.

Simple REST API endpoint /transcribe.

📦 Installation

Clone this repository:

git clone https://github.com/Ahmedaliuajk/Speech_to_text_AI_model.git
cd whisper-api


Create a virtual environment:

```python -m venv venv```
```venv\Scripts\activate  ```  # On Windows
#### OR
```source venv/bin/activate ```# On Mac/Linux


Install dependencies:

pip install -r requirements.txt

▶️ Run the API

Start the FastAPI server with:

``` python -m uvicorn main:app --reload ```

Server will start at:
```👉 http://127.0.0.1:8000```

You can open Swagger UI for testing:
```👉 http://127.0.0.1:8000/docs```

📡 API Endpoint
🔹 POST /transcribe

URL:

```http://127.0.0.1:8000/transcribe```


Input:

An audio file (file) sent as multipart/form-data.

Output (JSON):

{
  "language": "en",
  "text": "Hello, how are you?"
}

🧪 Example Usage
✅ Python Example
```
import requests

url = "http://127.0.0.1:8000/transcribe"
files = {"file": open("test.mp3", "rb")}
response = requests.post(url, files=files)

print(response.json())
```


📂 Project Structure
whisper_api/
│── main.py            # FastAPI app
│── requirements.txt   # Dependencies
│── README.md          # Documentation
