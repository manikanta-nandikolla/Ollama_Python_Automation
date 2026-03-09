# 🤖 AI Automation Assistant

A local AI-powered productivity assistant built with Python and Ollama.

This tool automates everyday tasks like:
- Email summarization
- Task extraction
- Meeting analysis
- File organization
- Desktop notifications
- Scheduled automation

All AI processing runs **locally** using Ollama and the Phi-3 model.

---

## 🚀 Features

### 📧 Email Automation
- Reads latest Gmail emails
- Summarizes emails using AI
- Extracts actionable tasks

### 🧠 Meeting Analysis
- Analyzes meeting notes
- Extracts:
  - Summary
  - Action items
  - Important decisions

### 📂 Smart File Organizer
Automatically organizes files into folders:
- PDFs
- Images
- Videos
- Others

### 🔔 Desktop Notifications
Shows system notifications for:
- Email summaries
- Meeting insights
- File organization updates

### ⏰ Scheduled Automation
Tasks run automatically using Python scheduler.

Example schedule:

| Task | Frequency |
|------|-----------|
| Email check | Every 1 hour |
| File organization | Every 30 minutes |
| Meeting analysis | Daily |

---

## 🏗 Project Structure
```
ai_automation_assistant/
│
├── main.py
├── notifier.py
│
├── email_task.py
├── meeting_task.py
├── file_task.py
│
├── gmail_reader.py
├── email_ai.py
├── meeting_ai.py
├── file_organizer.py
├── ollama_client.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 System Architecture
```
Gmail Inbox
     ↓
Python IMAP Reader
     ↓
Clean Email Text
     ↓
Ollama Local AI
     ↓
Summary / Tasks
     ↓
Desktop Notifications
```

---

## ⚙️ Requirements

- Python 3.10+
- Ollama installed
- Gmail App Password enabled

AI model used:
```
phi3
```

---

## 🛠 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/ai-automation-assistant.git
cd ai-automation-assistant
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate:

**Windows:**
```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Ollama

Download: https://ollama.com

Pull the model:
```bash
ollama pull phi3
```

### 5️⃣ Setup Environment Variables

Create a `.env` file:
```env
EMAIL=your_email@gmail.com
PASSWORD=your_gmail_app_password
```

---

## ▶️ Run the Assistant

Start automation:
```bash
python main.py
```

The assistant will run continuously and execute scheduled tasks.

---

## 📌 Example Output
```
AI AUTOMATION ASSISTANT STARTED

📧 Email Summary
Finish the Python automation script before Friday.

📂 File Organiser
Downloads folder organised successfully.
```

---

## 🔒 Security

Sensitive information is stored in `.env`, which is excluded from Git using `.gitignore`.

---

## 📈 Future Improvements

Planned upgrades:
- 🎙️ Voice commands
- 🤖 AI file classification
- 🌐 Web dashboard (FastAPI + React)
- 💬 WhatsApp automation
- 📅 Calendar integration

---

## 🧑‍💻 Author

**Manikanta**  
Python Developer | AI Automation Enthusiast

---

## ⭐ License

[MIT License](LICENSE)
