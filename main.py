from flask import Flask, request

app = Flask(__name__)

def convert_message(message):
    vowels = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    result = ''
    for char in message.lower():
        if char in vowels:
            result += vowels[char]
        elif char.isalpha():
            result += char + 'a'
        else:
            result += char
    return result

@app.route('/')
def home():
    return "WhatsApp Code Bot is Live!"

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    msg = data.get('message', '')
    return {'converted': convert_message(msg)}

if __name__ == '__main__':
    app.run()
