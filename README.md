# 🤖 AI CRM Chatbot

## 📌 Overview
This project is an AI-powered CRM chatbot built using Flask and OpenAI API. It is designed to handle customer queries such as refunds, complaints, and general support using conversational AI.

## 🚀 Features
- AI-based chatbot using OpenAI API
- Intent detection (refund, complaint, general queries)
- Context-based responses using RAG (Retrieval-Augmented Generation)
- Chat history tracking
- Web-based chat interface using HTML/CSS
- SQLite database integration for CRM data

## 🛠️ Tech Stack
- Python
- Flask
- OpenAI API
- SQLite
- HTML, CSS, JavaScript

## 📂 Project Structure
ai-crm-chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── rag.txt
├── requirements.txt
│
├── templates/
│ └── index.html
## ⚙️ How to Run

1. Clone the repository:

git clone <your-repo-link>
cd ai-crm-chatbot


2. Install dependencies:

pip install -r requirements.txt


3. Create a `.env` file:

OPENAI_API_KEY=your_api_key_here


4. Run the app:

python app.py


5. Open in browser:

http://127.0.0.1:5000/


## 🧠 How It Works
- User sends a message via web interface
- Flask backend processes the request
- Intent is detected (refund, complaint, general)
- Context is fetched from `rag.txt`
- OpenAI API generates response
- Response is sent back to user

## 🎯 Use Cases
- Customer support automation
- CRM systems
- AI-based virtual assistants

## 🔮 Future Improvements
- Add voice assistant support
- Integrate real CRM APIs
- Deploy on cloud (AWS/Render)
- Add user authentication

## 📌 Conclusion
This project demonstrates the integration of AI with web development to build an intelligent customer support system.
