# 🗣️ Voice-Guided Git Automation System

A **hybrid voice-controlled Git assistant** that allows developers to execute Git commands using natural speech.
This system combines **offline (Vosk), online (Google), and Whisper fallback** speech recognition to provide a fast, reliable, and hands-free Git workflow.

---

## 🚀 Features

* 🎤 **Hybrid Speech Recognition**

  * Offline: Vosk (fast streaming)
  * Online: Google Speech API
  * Fallback: Whisper (high accuracy)

* ⚡ **Real-Time Git Command Execution**

  * Add, commit, push, pull, branch, checkout, status

* 📂 **File-Specific Commit Support**

  * Example: `commit main.py`
  * Supports custom commit messages

* 🔐 **Optional Voice Authentication**

  * MFCC-based speaker verification

* 📊 **Live Dashboard**

  * Built using Streamlit
  * Real-time log monitoring

* 📝 **Robust Logging**

  * Detailed logs: `logs/commands.txt`
  * Short logs: `command_log.txt`

---

## 🏗️ Project Structure

```
voice_git_automation_final/
│
├── main.py                  # Voice controller
├── dashboard.py             # Streamlit dashboard
├── requirements.txt         # Dependencies
├── .gitignore
├── README.md
│
├── logs/
│   └── commands.txt         # Detailed logs
│
├── command_log.txt          # Short logs
│
├── auth/
│   └── voice_ref.wav        # Voice authentication reference (optional)
│
└── models/
    └── vosk-model-small-en-us-0.15/   # Vosk model
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/voice_git_automation_final.git
cd voice_git_automation_final
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

### 5️⃣ Download Vosk Model

* Visit: https://alphacephei.com/vosk/models
* Download: `vosk-model-small-en-us-0.15`
* Extract into:

```
models/vosk-model-small-en-us-0.15/
```

---

## 🔑 GitHub Authentication Setup

### ✅ Recommended: SSH

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Add the key to GitHub → **Settings → SSH and GPG Keys**

Set remote:

```bash
git remote set-url origin git@github.com:your-username/voice_git_automation_final.git
```

---

## ▶️ How to Run

### Start Voice Controller

```bash
python main.py
```

You will be asked to choose:

* **offline** → Vosk + Whisper fallback
* **online** → Google Speech API

---

### Start Dashboard (New Terminal)

```bash
streamlit run dashboard.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🎙️ Supported Voice Commands

| Command                               | Description                |
| ------------------------------------- | -------------------------- |
| commit                                | Commit all changes         |
| commit main.py                        | Commit specific file       |
| commit main.py with message "fix bug" | Commit with custom message |
| push                                  | Push to GitHub             |
| pull                                  | Pull latest changes        |
| status                                | Show repository status     |
| create branch dev                     | Create new branch          |
| switch to dev                         | Switch branch              |
| undo last commit                      | Undo last commit           |
| exit / quit                           | Stop program               |

---

## 🔄 ASR Modes

| Mode    | Description                  |
| ------- | ---------------------------- |
| Offline | Fast Vosk + Whisper fallback |
| Online  | Google Speech Recognition    |

---

## 📊 Dashboard Features

* Real-time command logs
* Execution tracking
* Debug monitoring

Files used:

```
command_log.txt
logs/commands.txt
```

---

## 🛠️ Troubleshooting

### 🎤 Microphone Not Working

```python
import sounddevice as sd
print(sd.query_devices())
```

---

### ❌ Git Push Failed

```bash
git remote -v
```

✔ Use SSH instead of HTTPS for best results

---

### 🐢 Whisper is Slow

Set:

```
WHISPER_MODEL = "tiny"
```

---

### ⚠️ Vosk Not Detecting Speech

* Ensure microphone supports **16kHz**
* Try changing device index

---

## 🚫 Ignored Files

```
logs/
command_log.txt
*.wav
venv/
__pycache__/
```

---

## 📦 Creating a Release

1. Go to **GitHub → Releases**
2. Click **Draft new release**
3. Add tag:

```
v1.0.0
```

4. Add title & description
5. Publish

---

## 🎓 Use Cases

* Hands-free Git operations
* Developer productivity improvement
* Accessibility for developers
* Voice-controlled DevOps workflows

---

## 🔮 Future Enhancements

* Multi-file commit via voice
* VS Code Extension
* GitHub Pull Request automation
* AI-based command suggestions

---

## 👩‍💻 Author

**Khushi Goda**

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🚀 Contribute

---

## 🧠 Summary

This project demonstrates a **real-world integration of AI and DevOps**, combining:

* Speech Recognition
* Natural Language Processing
* Git Automation
* Real-Time Dashboard

---

🔥 A powerful step towards **hands-free development workflows**
