from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Olá! Aplicação Flask funcionando.'})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({'you_sent': data})

if __name__ == '__main__':
    app.run(debug=True)
