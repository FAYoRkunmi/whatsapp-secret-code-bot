from flask import Flask, request, jsonify

app = Flask(__name__)

# Secret code function
def secret_code(text):
    code = ""
    for char in text:
        if char.lower() in "aeiou":
            code += {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}[char.lower()]
        elif char.isalpha():
            code += char + "a"
        else:
            code += char
    return code

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Secret Code Bot is live!"

@app.route("/encode", methods=["POST"])
def encode():
    data = request.get_json()
    message = data.get("message", "")
    result = secret_code(message)
    return jsonify({"original": message, "encoded": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)