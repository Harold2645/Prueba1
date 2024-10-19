from flask import render_template, send_from_directory, session, url_for
from conexion import *
from routes.usuarios import *
from routes.novedades import *
from routes.categorias import *
from routes.insumos import *
from routes.tractores import *
from routes.herramientas import *
from routes.liquidos import *
from routes.graficos import *
from routes.enviosConsu import *
from routes.servicios import *
from ionic import *

@app.route('/uploads/<nombre>')
def uploads(nombre):
    return send_from_directory(app.config['CARPETAU'],nombre)

@app.route('/')
def index():
    session["loginCorrecto"] = False
    return render_template('/index.html') 

@app.errorhandler(404)
def not_found(error):
    # return redirect(url_for('404.html'))
    return render_template('404.html'), 404

@app.route('/consultarol', methods=['POST'])
def consultarol():
    data = request.get_json()
    # documento = data["documento"]
    if len(data)>0:
        sql = f"SELECT rol FROM usuarios WHERE documento='{data}'"
        cur = conexion.cursor()
        cur.execute(sql)
        resultado = cur.fetchone()
        if resultado:
            return resultado[0]
        else:
            return "No existe"
    else:
        return "Error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5001")