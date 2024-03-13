from flask import render_template, send_from_directory, session
from conexion import *
from routes.usuarios import *
from routes.novedades import *
from routes.categorias import *
from routes.inventario import *

@app.route('/uploads/<nombre>')
def uploads(nombre):
    return send_from_directory(app.config['CARPETAU'],nombre)

@app.route('/')
def index():
    session["logueado"] = False
    return render_template('/index.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")