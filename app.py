from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    user_message = data.get('message', '')
    response_message = f"Você disse: {user_message}"
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)