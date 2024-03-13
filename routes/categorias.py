from conexion import *
from flask import redirect, render_template, request, session
from models.funciones import misCategorias

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
        return render_template("lideres/categorias/categoriaAg.html")
    else:
        return redirect('/')

@app.route('/guardarCategoria', methods=['POST'])
def guardarCategoria():
    nombre = request.form['nombre_categoria']
    tipo = request.form['tipo_categoria']
    misCategorias.agregarCategoria([nombre, tipo])
    return redirect("/consultarCategorias")

#borrar categorias
@app.route('/borrarCategoria/<idCategoria>')
def borrarCategoria(idCategoria):
    misCategorias.borrarCategoria(idCategoria)
    return redirect('/consultarCategorias')
    