from flask import redirect, render_template, request, session
from conexion import *
from models.inventario import misHerramientas, misInsumos, misLiquidos, misTracores
from models.funciones import misCategorias


@app.route('/consultarTractores')
def consultaTractores():
    if session.get("loginCorrecto"):
        resultado = misTracores.todoslosTractores()
        return render_template("lideres/tractores/verTractores.html", res=resultado)
    else:
        return redirect('/')

#agregar tractores
@app.route("/agregarTractor")
def agregaarticulo():
    if session.get("loginCorrecto"):
        categorias = misCategorias.categoriasTractor()
        return render_template("lideres/tractores/tractoresAg.html", categorias=categorias)
    else:
        return redirect('/')

@app.route("/guardarTractor" ,methods=['POST'])
def guardararticulo():
    idObjeto = request.form['id_tractor']
    nombre = request.form['nombre']
    idCategoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    if misTracores.buscar(idObjeto):
        categorias = misCategorias.categoriasTractor()
        return render_template("lideres/tractores/tractoresAg.html", msg="Id ya existente", categorias=categorias)
    else:
        misTracores.agregar([idObjeto,nombre,idCategoria,estado,disponibilidad])
        return redirect("/consultarTractores")

#borrar tractores 
@app.route('/borrarTractor/<idObjetos>')
def borrarTractor(idObjetos):
    misTracores.borrar(idObjetos)
    return redirect('/')

#editar tractores
@app.route('/editarTractor/<idObjeto>')
def editarTractor(idObjeto):
    if session.get("loginCorrecto"):
        tractor = misTracores.buscar(idObjeto)
        categorias = misCategorias.categoriasTractor()
        return render_template("lideres/tractores/tractoresEd.html",tractor=tractor[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarTractor', methods=['POST'])
def actualizarTractor():
    idObjeto = request.form['id_tractor']
    nombre = request.form['nombre']
    categoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    activo = request.form['activo']
    modif = [idObjeto,nombre,categoria,estado,disponibilidad,activo]
    misTracores.modificar(modif)
    return redirect("/consultarTractores")


#herramientas
@app.route('/consultarHerramientas')
def consultaHerramientas():
    if session.get("loginCorrecto"):
        rol = session['rol']
        resultado = misHerramientas.consultarHerramientas()
        if rol == 'Aprendiz':
            return render_template('Aprendiz/herramientasA.html', res=resultado)
        elif rol == 'Instructor':
            return render_template("Instructor/herramientaIns.html", res=resultado)
        elif rol == 'Admin':
            return render_template("herramientas/herramientas.html", res=resultado)
    else:
        return redirect('/')

@app.route('/consultarlasHerramientas')
def consultalasHerramientas():
    if session.get("loginCorrecto"):
        resultado = misHerramientas.todaslasHerramientas()
        return render_template("herramientas/todaslasHerramientas.html", res=resultado)
    else:
        return redirect('/')

#agregar herramientas
@app.route("/agregarHerramienta")
def agregarHerramienta():
    if session.get("loginCorrecto"):
        categorias = misCategorias.categoriasHerramienta()
        return render_template("herramientas/agregarHerramientas.html", categorias=categorias)
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
        return render_template("herramientas/agregarHerramienta.html", msg="Id ya existente", categorias=categorias)
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
        return render_template("herramientas/modificarherramienta.html",herramienta=herramienta[0], categorias=categorias)
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