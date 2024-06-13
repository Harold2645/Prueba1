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
<<<<<<< HEAD
from prueba_json import *
=======


>>>>>>> bb083afb6324e7935dfd6f5e195c65d67200a90c

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5080")