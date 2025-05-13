# 🤖 Genesis-AI-Voice-Assistant

**Genesis** is an intelligent voice assistant powered by **LiveKit** and **OpenAI** APIs. It enables real-time, voice-driven interaction with contextual responses and functional commands — perfect for building smart, conversational AI experiences.


## ✨ Features

- **🎙️ Real-time voice interaction using LiveKit Rooms** 
- **🧠 Context-aware responses using OpenAI's LLMs**  
- **🏠 Smart environment control (e.g., zone-specific temperature)**
- **🗣️ Natural conversation flow via Silero Voice Activity Detection (VAD)**  
- **🔌 Easily extendable function hooks**


## 📁 Project Structure

```planetext
Genesis-AI/
├── api/
│   ├── __init__.py              # 📦 Initializes the API module
│   └── assistant_fnc.py         # 🧠 Functional logic (e.g., temperature control)
├── genesis.py                   # 🚀 Main entry point for Genesis assistant
│                                # 👉 Run it with: python genesis.py
├── .env.example                 # 🔐 Template for environment variables
│                                # 👉 Rename and configure: cp .env.example .env
├── .gitignore                   # 🛡️ Hides sensitive files from Git
│                                # 👉 Includes: .env, __pycache__/, *.pyc, etc.
├── requirements.txt             # 📦 Python dependency list
│                                # 👉 Install with: pip install -r requirements.txt
├── LICENSE                      # 📄 MIT License (permits open use & distribution)
└── README.md                    # 📘 Full documentation and usage instructions
```

## ⚙️ Installation Guide

> 💡 Make sure you have **Python 3.9+** installed.

### 🔽 1. Clone the Repo

```bash
git clone https://github.com/your-username/Genesis-AI-Voice-Assistant.git
cd Genesis-AI-Voice-Assistant
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🧾 3. Configure Environment Variables

**Copy** `sample.env` **and rename it to** `.env` **:**

```bash
cp sample.env .env
```

**Then update it with your credentials:**

```env
LIVEKIT_URL=" "
LIVEKIT_API_KEY=" "
LIVEKIT_API_SECRET=" "
OPENAI_API_KEY=" "
```

## 🚀 Getting Started

**To run the assistant:**

```bash
python main.py
```

**If configured correctly, you’ll hear:**

> "Hey, how can I help you today!"

## 🛠️ Tech Stack
| Tool              | Description                                      |
| ----------------- | ------------------------------------------------ |
| 🟪 **LiveKit**    | Real-time audio streaming and room management    |
| 🧠 **OpenAI**     | ChatGPT, Speech-to-Text, and Text-to-Speech APIs |
| 🔉 **Silero VAD** | Voice Activity Detection for natural flow        |
| 🐍 **Python**     | Language for backend logic and orchestration     |


## 📚 Learn More

-📄 LiveKit Documentation

-📘 OpenAI API Docs

-🧠 Silero VAD

## 📄 License

Licensed under the **MIT License**.
See the **LICENSE** file for details.

## 👤 Author

**Arshanth Kumar**

**🔗 GitHub**: @4rshxnth
