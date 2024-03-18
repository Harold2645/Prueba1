from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.herramientas import misHerramientas




#herramientas
@app.route('/consultarHerramientas')
def consultaHerramientas():
    if session.get("loginCorrecto"):
        rol = session['rol']
        resultado = misHerramientas.consultarHerramientas()
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/herramientas.html', res=resultado)
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/herramientas/herramientas.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/consultarlasHerramientas')
def consultalasHerramientas():
    if session.get("loginCorrecto"):
        resultado = misHerramientas.todaslasHerramientas()
        return render_template("lideres/herramientas/verHerramientas.html", res=resultado)
    else:
        return redirect('/')

#agregar herramientas
@app.route("/agregarHerramienta")
def agregarHerramienta():
    if session.get("loginCorrecto"):
        categorias = misCategorias.categoriasHerramienta()
        return render_template("lideres/herramientas/herramientasAg.html", categorias=categorias)
    else:
        return redirect('/')

@app.route("/guardarHerramienta" ,methods=['POST'])
def guardarHerramienta():
    idObjeto = request.form['id_herramienta']
    nombre = request.form['nombre']
    idCategoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    if misHerramientas.buscar(idObjeto):
        categorias = misCategorias.categoriasTractor()
        return render_template("lideres/herramientas/herramientasAg.html", msg="Id ya existente", categorias=categorias)
    else:
        misHerramientas.agregar([idObjeto,nombre,idCategoria,estado,disponibilidad])
        return redirect("/consultarHerramientas")

#borrar Herramientas 
@app.route('/borrarHerramienta/<idObjetos>')
def borrarHerramienta(idObjetos):
    misHerramientas.borrar(idObjetos)
    return redirect('/consultarHerramientas')

#editar Herramientas
@app.route('/editarHerramienta/<idObjeto>')
def editarHerramienta(idObjeto):
    if session.get("loginCorrecto"):
        herramienta = misHerramientas.buscar(idObjeto)
        categorias = misCategorias.categoriasHerramienta()
        return render_template("lideres/herramientas/herramientasEd.html",herramienta=herramienta[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarHerramienta', methods=['POST'])
def actualizarHerramienta():
    idObjeto = request.form['id_herramienta']
    nombre = request.form['nombre']
    categoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    activo = request.form['activo']
    modif = [idObjeto,nombre,categoria,estado,disponibilidad,activo]
    misHerramientas.modificar(modif)
    return redirect("/consultaHerramientas")

