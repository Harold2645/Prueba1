from flask import render_template, send_from_directory, session
from conexion import *
from routes.usuarios import *
from routes.novedades import *
from routes.categorias import *
from routes.insumos import *
from routes.tractores import *
from routes.herramientas import *
from routes.liquidos import *


@app.route('/uploads/<nombre>')
def uploads(nombre):
    return send_from_directory(app.config['CARPETAU'],nombre)

@app.route('/')
def index():
    session["logueado"] = False
    return render_template('/index.html') 

@app.route('/funciones')
def funciones():
    return render_template("funciones.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")