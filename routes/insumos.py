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
        nombre = session['nombreUsuario']
        resultado = misInsumos.consultarinsumos()
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/insumos.html', res=resultado,nombreusu=nombre, rolusu=rol)
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/insumos/insumos.html", res=resultado,nombreusu=nombre, rolusu=rol)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/consultarlosConsumibles')
def consultalarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misInsumos.todoslosinsumos()
            return render_template("lideres/insumos/verInsumos.html", res=resultado,nombreusu=nombre, rolusu=rol ,)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/buscarInsumo', methods=['GET', 'POST'])
def buscarInsumo():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        nombreUsu = session['nombreUsuario']
        if request.method == "POST":
            nombre = request.form['buscar_insumo']
            resultado = misInsumos.buscarPornombre(nombre)
            return render_template("usuarios/insumos.html", res=resultado, nombreusu=nombreUsu, rolusu=rol)
        else:
            return redirect('/')
    else:
        return redirect('/')

# agregar Consumibles
@app.route("/agregarConsumibles")
def agregarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            categorias = misCategorias.categoriasInsumos()
            return render_template("lideres/insumos/insumosAg.html", categorias=categorias,nombreusu=nombre, rolusu=rol)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarConsumibles" ,methods=['POST'])
def guardarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
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
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# borrar Consumibles 
@app.route('/borrarConsumibles/<idObjetos>')
def borrarConsumibles(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            misInsumos.borrar(idObjetos)

            # nombre = misInsumos.buscarnombre(idObjetos)
            # creador = session['documento'] 
            # movimiento = "BorroInsumo"
            # misMovimientos.agregar([creador, movimiento, nombre])
            return redirect('/consultarConsumibles')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# editar Consumibles
@app.route('/editarConsumibles/<idObjeto>')
def editarConsumibles(idObjeto):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            Consumible = misInsumos.buscar(idObjeto)
            categorias = misCategorias.categoriasInsumos()
            return render_template("lideres/insumos/insumosEd.html",Consu=Consumible[0], categorias=categorias,nombreusu=nombre, rolusu=rol)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/actualizarConsumibles', methods=['POST'])
def actualizarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            idobjeto = request.form['idobjeto']
            nombre = request.form['nombre']
            categoria = request.form.get('id_categoria')
            cantidad = request.form['cantidad']
            foto = request.files['foto']
            
            if len(request.form['activo']) == 0:
                activo = 1
            else:
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
            misMovimientos.agregar([creador, movimiento, idobjeto])
            return redirect("/consultarConsumibles")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

