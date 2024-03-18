from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.insumos import misInsumos


#Consumibles

#mostrar consumibles
@app.route('/consultarConsumibles')
def consultaConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        resultado = misInsumos.consultarinsumos()
        if rol == 'Aprendiz':
            return render_template('Aprendiz/consumiblesA.html', res=resultado)
        elif rol == 'Instructor':
            return render_template("Instructor/consumiblesIns.html", res=resultado)
        elif rol == 'Admin':
            return render_template("consumibles/consumibles.html", res=resultado)
    else:
        return redirect('/')
    
@app.route('/consultarlosConsumibles')
def consultalarConsumibles():
    if session.get("loginCorrecto"):
        resultado = misInsumos.todoslosinsumos()
        return render_template("consumibles/todaslasConsumibles.html", res=resultado)
    else:
        return redirect('/')

#agregar Consumibles
@app.route("/agregarConsumibles")
def agregarConsumibles():
    if session.get("loginCorrecto"):
        categorias = misCategorias.categoriasConsumibles()
        return render_template("consumibles/agregarConsumibles.html", categorias=categorias)
    else:
        return redirect('/')

@app.route("/guardarConsumibles" ,methods=['POST'])
def guardarConsumibles():
    idObjeto = request.form['id_Consumible']
    nombre = request.form['nombre']
    idCategoria = request.form.get('id_categoria')
    cantidad = request.form['cantidad']
    if misInsumos.buscar(idObjeto):
        categorias = misCategorias.categoriasTractor()
        return render_template("consumibles/agregarConsumible.html", msg="Id ya existente", categorias=categorias)
    else:
        misInsumos.agregar([idObjeto,nombre,idCategoria,cantidad])
        return redirect("/consultarConsumibles")

#borrar Consumibles 
@app.route('/borrarConsumibles/<idObjetos>')
def borrarConsumibles(idObjetos):
    misInsumos.borrar(idObjetos)
    return redirect('/consultarConsumibles')

#editar Consumibles
@app.route('/editarConsumibles/<idObjeto>')
def editarConsumibles(idObjeto):
    if session.get("loginCorrecto"):
        Consu = misInsumos.buscar(idObjeto)
        categorias = misCategorias.categoriasConsumibles()
        return render_template("consumibles/modificarConsumibles.html",Consu=Consu[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarConsumibles', methods=['POST'])
def actualizarConsumibles():
    idObjeto = request.form['id_Consumible']
    nombre = request.form['nombre']
    categoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    activo = request.form['activo']
    modif = [idObjeto,nombre,categoria,estado,disponibilidad,activo]
    misInsumos.modificar(modif)
    return redirect("/consultarConsumibles")