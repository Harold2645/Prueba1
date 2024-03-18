from datetime import datetime
from conexion import *
from flask import redirect, render_template, request, session
from models.categorias import misCategorias

#categorias

#mostrar categorias
@app.route('/consultarCategorias')
def consultaCategorias():
    if session.get("loginCorrecto"):
        resultado = misCategorias.consultarCategorias()
        return render_template("lideres/categorias/categoria.html", res=resultado)
    else:
        return redirect('/')

#agregar  categorias 
@app.route('/agregarCategoria')
def agregarCategoria():
    if session.get("loginCorrecto"):
        descripcion = misCategorias.buscarCate()
        descri = [descrip[0] for descrip in descripcion]
        return render_template("lideres/categorias/categoriaAg.html", descripciones=descri)
    else:
        return redirect('/')

@app.route('/guardarCategoria', methods=['POST'])
def guardarCategoria():
    nombre = request.form['nombre_categoria']
    tipo = request.form['tipo_categoria']
    descripcion = request.form['descripcion']
    ahora = datetime.now()
    fecha = ahora.strftime("%Y%m%d%H%M%S")
    documento = session['documento']
    creador = documento
    misCategorias.agregarCategoria([nombre, tipo, descripcion, fecha, creador])
    return redirect("/consultarCategorias")

#borrar categorias
@app.route('/borrarCategoria/<idCategoria>')
def borrarCategoria(idCategoria):
    misCategorias.borrarCategoria(idCategoria)
    return redirect('/consultarCategorias')
    