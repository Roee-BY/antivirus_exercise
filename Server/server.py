from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []

@app.route('/logs', methods=['POST'])
def add_log():
    data = request.json
    if 'message' in data:
        logs.append(data)
        return jsonify({'message': 'Log added successfully'}), 200
    else:
        return jsonify({'error': 'No message provided'}), 400

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200

if __name__ == '__main__':
    app.run()
