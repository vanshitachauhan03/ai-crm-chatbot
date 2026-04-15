from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from database import create_db

app = Flask(__name__)

create_db()

chat_history = []

def detect_intent(msg):
    msg = msg.lower()
    if "refund" in msg:
        return "refund"
    elif "problem" in msg:
        return "complaint"
    return "general"

def get_context():
    with open("rag.txt", "r") as f:
        return f.read()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data["message"]

    intent = detect_intent(user_msg)
    context = get_context()

    reply = get_response(user_msg, context, chat_history)

    chat_history.append({"user": user_msg, "bot": reply})

    return jsonify({
        "reply": reply,
        "intent": intent
    })

if __name__ == "__main__":
    app.run(debug=True)
