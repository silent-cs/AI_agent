from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai 
load_dotenv()
app = Flask(__name__)

# إعداد Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        user_input = request.form["user_input"]
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        chat = model.start_chat(history=[])
        reply = chat.send_message(user_input)
        response = reply.text
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
