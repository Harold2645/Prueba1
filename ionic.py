from conexion import *
from flask import Flask, jsonify, request
from flask_cors import CORS
from models.usuarios import misUsuarios
import json


@app.route('/consultaUsuarioIonic', methods=['GET'])
def consultaUsuarioIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE activo=1")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    # res = misUsuarios.consultar()
    # return json.dump(res)


@app.route('/registrarUsuarioIonic', methods=['POST'])
def registrarUsuarioIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuario (documento, nombre, apellido, celular) VALUES (%s, %s, %s, %s)", (data['documento'], data['nombre'], data['apellido'], data['celular']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})  
    

@app.route('/consultaTractoresIonic', methods=['GET'])
def consultaTractoresIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("SELECT tractores.marca, tractores.modelo, tractores.idobjeto, tractores.idcategoria, tractores.fototrac, tractores.activo, categorias.idcategoria, categorias.nombre, categorias.tipo FROM tractores INNER JOIN categorias WHERE tractores.idcategoria = categorias.idcategoria AND tractores.activo = '1' AND categorias.tipo = 'Tractor';")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/misPedidos/<id>', methods=['GET'])
def misPedidos(id):
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute (f"SELECT * FROM (SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.documento = {id} UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.documento = {id} UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.documento = {id}) AS combined_results ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        if(len(datos)==0):
            cursor.close()
            connection.close()
            return jsonify({"msg":"notFound"})
        else:
            cursor.close()
            connection.close()
            return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})  