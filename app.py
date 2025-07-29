from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API key setup
genai.configure(api_key="AIzaSyCUW4hRnRShZQslH4gefugOnG55cvBgMK8")
model = genai.GenerativeModel("gemini-2.5-pro")

# ✅ Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Chat Assistant route
@app.route('/assistant')
def assistant():
    return render_template('chat.html')

# ✅ About page route
@app.route('/about')
def about():
    return render_template('about.html')

# ✅ Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# ✅ AI Chat POST handler
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = "❌ Something went wrong. Try again later."
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
