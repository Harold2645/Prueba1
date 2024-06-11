import json 
from flask import request
from flask import Flask,render_template, jsonify

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/microservicio', methods=['GET'])
def microservicio():
    documento = request.get_json()
    print("Aqui recoge: ",documento)
    
    resultado = json.JSONEncoder().encode(documento)
    print("Aqui envia: ",resultado)

    return resultado

    




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")