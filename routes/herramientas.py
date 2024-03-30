from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.herramientas import misHerramientas
from models.movimientos import misMovimientos




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
    documento = session['documento'] 
    idobjeto = request.form['id_herramienta']
    idcategoria = request.form.get('id_categoria')
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    foto = request.files['foto']
    ahora = datetime.now()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    creador = documento
    if misHerramientas.buscar(idobjeto):
        categorias = misCategorias.categoriasHerramienta()
        return render_template("lideres/herramientas/herramientasAg.html", msg="Id ya existente", categorias=categorias)
    else:
        fnombre,fextension = os.path.splitext(foto.filename)
        nombreFoto = "H"+ahora.strftime("%Y%m%d%H%M%S")+fextension
        foto.save("uploads/"+nombreFoto)
        misHerramientas.agregar([idobjeto,idcategoria,nombre,cantidad,nombreFoto,fecha,creador])

        movimiento = "AgregoHerramienta"
        misMovimientos.agregar([creador, movimiento, idobjeto])

        return redirect("/consultarHerramientas")

#borrar Herramientas 
@app.route('/borrarHerramienta/<idObjetos>')
def borrarHerramienta(idObjetos):
    misHerramientas.borrar(idObjetos)

    idobjeto = idObjetos
    creador = session['documento'] 
    movimiento = "BorroHerramienta"
    misMovimientos.agregar([creador, movimiento, idobjeto])

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
    foto = request.files['foto']
    ahora = datetime.now()
    fnombre,fextension = os.path.splitext(foto.filename)
    nombreFoto = "H"+ahora.strftime("%Y%m%d%H%M%S")+fextension
    foto.save("uploads/"+nombreFoto)
    misHerramientas.modificar([idObjeto,nombre,categoria,nombreFoto])

    creador = session['documento'] 
    movimiento = "EditoHerramienta"
    misMovimientos.agregar([creador, movimiento, idObjeto])

    return redirect("/consultarHerramientas")


#urbano aqui hago la funcion para mostrar solo lo que el usuario 

@app.route('/buscarHerramientas', methods=['POST'])
def buscarHerramientas():
    if session.get("loginCorrecto"):
        termino_busqueda = request.form.get('buscar_herramientas', '').strip()
        resultado = misHerramientas.buscarPornombre(termino_busqueda)
        return render_template("usuarios/herramientas.html", res=resultado)
    else:
        return redirect('/')
