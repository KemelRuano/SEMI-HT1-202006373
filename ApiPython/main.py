from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return "OK" , 200

@app.route('/check', methods=['GET'])
def check():
    Message = {
        "Instancia": "Instancia #2 - API #2",
        "Curso":"Seminario de Sistemas 1",
        "Estudiante":"Estudiante - <202006373>"
    }
    return jsonify(Message), 200

if __name__ == '__main__':
    app.run( host= '0.0.0.0' , debug=True , port=8081)
