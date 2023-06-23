from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
