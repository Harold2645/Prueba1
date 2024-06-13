import json
from flask import  request
from conexion import *


@app.route("/peticion")
def peticion():
    respuesta = {
        "msg": "Hola mundo"
    }
    return respuesta

@app.route("/microservicio", methods=['POST'])
def microservicio():
    # documento = requests.post['usuario']
    documento = request.get_json()
    print("Este es el documento",documento)

    resultado = json.loads(documento)
    print("Este es el resultado",documento)


    sql = f"SELECT rol FROM usuarios WHERE documento='{documento}'"
    cur = conexion.cursor()
    cur.execute(sql)
    resultado = cur.fetchone()
    respuesta = {
        "Rol": resultado
    }
    return respuesta   

@app.route("/peticion_prueba", methods=['POST'])
def peticion_prueba():
    documento = request.get_json().get('usuario')

    if len(documento) >= 6 & len(documento) <= 15:
        sql = f"SELECT rol FROM usuarios WHERE documento='{documento}'"
        cur = conexion.cursor()
        cur.execute(sql)
        resultado = cur.fetchall()

        microrespuesta = {
            'valor': resultado
        }

        return microrespuesta

    else: 
        microrespuesta = {"valor:" 'NO'}
        return microrespuesta

@app.route('/peticion_forma_prueba', methods=['POST'])
def promedio():
    try:
        documento = request.get_json().get('usuario')
        connection = conexion()
        cursor = connection.cursor()
        cursor.execute (f"SELECT ROUND(AVG(puntaje)) AS promedio FROM calificacion WHERE idcontratista = {documento}")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        if(len(datos)==0):
            cursor.close()
            connection.close()
            return json.loads({"msg":"No hay"})
        else:
            cursor.close()
            connection.close()
            return json.loads([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return json.loads({"error": str(e)})  
    


@app.route('/prueba', methods=['POST'])
def prueba():
    documento = request.get_json().get('usuario')
    print(documento)
    connection = conexion()
    cursor = connection.cursor()
    cursor.execute (f"SELECT ROUND(AVG(puntaje)) AS promedio FROM calificacion WHERE idcontratista = {documento}")
    datos = cursor.fetchall()
    cursor.close()
    connection.close()
    print(datos)
    return json.loads(datos)



