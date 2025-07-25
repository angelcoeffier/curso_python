from flask import Flask, request, jsonify
from cliente import cliente

app = Flask(__name__)

app.register_blueprint(cliente)

@app.route('/', methods=['GET'])

def unida():
    return "Server is running in port 5003"

if __name__ == '__main__':
    app.run(debug=True, port=5003)