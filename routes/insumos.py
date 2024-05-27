from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.insumos import misInsumos
from models.movimientos import misMovimientos

# Consumibles

# mostrar consumibles
@app.route('/consultarConsumibles')
def consultaConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        resultado = misInsumos.consultarinsumos()
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/insumos.html', res=resultado)
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/insumos/insumos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/consultarlosConsumibles')
def consultalarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misInsumos.todoslosinsumos()
            return render_template("lideres/insumos/verInsumos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# agregar Consumibles
@app.route("/agregarConsumibles")
def agregarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            categorias = misCategorias.categoriasInsumos()
            return render_template("lideres/insumos/insumosAg.html", categorias=categorias)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarConsumibles" ,methods=['POST'])
def guardarConsumibles():
    if session.get("loginCorrecto"):
        documento = session['documento'] 
        idCategoria = request.form.get('id_categoria')
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        foto = request.files['foto']
        ahora = datetime.now()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        creador = documento
        fnombre,fextension = os.path.splitext(foto.filename)
        nombreFoto = "I"+ahora.strftime("%Y%m%d%H%M%S")+fextension
        foto.save("uploads/"+nombreFoto)
        misInsumos.agregar([idCategoria,nombre,cantidad,nombreFoto,fecha,creador])

        movimiento = "AgregoInsumo"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect("/consultarConsumibles")
    else:
        return redirect('/')

# borrar Consumibles 
@app.route('/borrarConsumibles/<idObjetos>')
def borrarConsumibles(idObjetos):
    if session.get("loginCorrecto"):
        misInsumos.borrar(idObjetos)

        nombre = misInsumos.buscarnombre(idObjetos)
        creador = session['documento'] 
        movimiento = "BorroInsumo"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect('/consultarConsumibles')
    else:
        return redirect('/')

# editar Consumibles
@app.route('/editarConsumibles/<idObjeto>')
def editarConsumibles(idObjeto):
    if session.get("loginCorrecto"):
        Consumible = misInsumos.buscar(idObjeto)
        categorias = misCategorias.categoriasInsumos()
        return render_template("lideres/insumos/insumosEd.html",Consu=Consumible[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarConsumibles', methods=['POST'])
def actualizarConsumibles():
    if session.get("loginCorrecto"):
        idobjeto = request.form['idobjeto']
        nombre = request.form['nombre']
        categoria = request.form.get('id_categoria')
        cantidad = request.form['cantidad']
        foto = request.files['foto']
        activo = request.form['activo']
        if foto.filename == '':
            foto1 = request.form['foto1']
            misInsumos.modificar([idobjeto,nombre,categoria,cantidad, foto1, activo])
        else:
            ahora = datetime.now()
            fnombre,fextension = os.path.splitext(foto.filename)
            nombreFoto = "I"+ahora.strftime("%Y%m%d%H%M%S")+fextension
            foto.save("uploads/"+nombreFoto)
            misInsumos.modificar([idobjeto,nombre,categoria,cantidad, nombreFoto, activo])

        creador = session['documento'] 
        movimiento = "EditoInsumo"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect("/consultarConsumibles")
    else:
        return redirect('/')

@app.route('/buscarLiquido', methods=['POST'])
def buscarLiquido():
    if session.get("loginCorrecto"):
        termino_busqueda = request.form.get('buscar_insumo', '').strip()
        resultado = misInsumos.buscarPornombre(termino_busqueda)
        return render_template("usuarios/insumos.html", res=resultado)
    else:
        return redirect('/')
