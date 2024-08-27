from datetime import datetime
from conexion import *
from flask import redirect, render_template, request, session
from models.categorias import misCategorias

# categorias

# mostrar categorias
@app.route('/consultarCategorias')
def consultaCategorias():
    if session.get("loginCorrecto"):
        rol = session['rol']
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misCategorias.consultarCategorias()
            return render_template("lideres/categorias/categoria.html", res=resultado,nombreusu=nombre  , rolusu=rol )
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# agregar categorias 
@app.route('/agregarCategoria')
def agregarCategoria():
    if session.get("loginCorrecto"):
        rol = session['rol']
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            descripcion = misCategorias.buscarCate()
            descri = [descrip[0] for descrip in descripcion]
            return render_template("lideres/categorias/categoriaAg.html", descripciones=descri,nombreusu=nombre, rolusu=rol)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/guardarCategoria', methods=['POST'])
def guardarCategoria():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            nombre = request.form['nombre_categoria']
            tipo = request.form['tipo_categoria']
            descripcion = request.form['descripcion']
            ahora = datetime.now()
            fecha = ahora.strftime("%Y%m%d%H%M%S")
            documento = session['documento']
            creador = documento
            misCategorias.agregarCategoria([nombre, tipo, descripcion, fecha, creador])
            return redirect("/consultarCategorias")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# borrar categorias
@app.route('/borrarCategoria/<idCategoria>')
def borrarCategoria(idCategoria):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            misCategorias.borrarCategoria(idCategoria)
            return redirect('/consultarCategorias')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
# Activar categorias
@app.route('/activarCategoria/<idCategoria>')
def activarCategoria(idCategoria):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            misCategorias.activarCategoria(idCategoria)
            return redirect('/consultarCategorias')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

