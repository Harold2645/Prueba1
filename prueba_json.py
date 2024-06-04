from flask import request
from conexion import *

@app.route("/peticion")
def peticion():
    respuesta = {
        "msg": "Hola mundo"
    }
    return respuesta

@app.route("/peticion_forma", methods=['POST'])
def peticion_forma():
    documento = request.form['usuario']

    sql = f"SELECT rol FROM usuarios WHERE documento='{documento}'"
    cur = conexion.cursor()
    cur.execute(sql)
    resultado = cur.fetchone()

    respuesta = {
        "Rol": resultado
    }

    return respuesta
