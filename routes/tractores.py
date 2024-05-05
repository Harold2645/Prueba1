from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.tractores import misTracores
from models.movimientos import misMovimientos


#Tractores
@app.route('/tractores')
def tractores():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        resultado = misTracores.mostarTractores()
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/tractores.html', res=resultado)
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template('lideres/tractores/tractores.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

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

@app.route("/guardarTractor",   methods=['POST'])
def agregarTrac():
    if session.get("loginCorrecto"):
        creador = session['documento'] 
        idobjeto = request.form['idobjeto']
        categoria = request.form['idcategoria']
        foto = request.files['fototrac']
        hora = datetime.now()
        fechacreacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        marca = request.form['marca']
        modelo = request.form['modelo']
        if misTracores.buscar(idobjeto):
            categorias = misCategorias.categoriasTractor()
            return render_template("lideres/tractores/tractoresAg.html", categorias=categorias, msg="Id ya existente")
        else:
            fnombre,fextension = os.path.splitext(foto.filename)  
            fotot = "T"+hora.strftime("%Y%m%d%H%M%S")+fextension        
            foto.save("uploads/" + fotot)
            misTracores.agregar([idobjeto, categoria, fotot, fechacreacion, creador,marca, modelo])
                    #funcion de guardar en tabla movimientos
            movimiento = "AgregoTractor"
            misMovimientos.agregar([creador, movimiento, idobjeto])
            return redirect("/tractores")
    else:
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
    if session.get("loginCorrecto"):
        idobjeto = request.form['id_tractor']
        categoria = request.form['id_categoria']
        marca = request.form['marca']
        modelo = request.form['modelo']
        foto = request.files['fototrac']
        hora = datetime.now()
        fnombre,fextension = os.path.splitext(foto.filename)  
        fotot = "T"+hora.strftime("%Y%m%d%H%M%S")+fextension        
        foto.save("uploads/" + fotot)
        misTracores.modificar([idobjeto, categoria, fotot, marca, modelo])

        creador = session['documento'] 
        movimiento = "EditoTractor"
        misMovimientos.agregar([creador, movimiento, idobjeto])
        return redirect("/consultarTractores")
    else:
        return redirect('/')

#borrar tractores 
@app.route('/borrarTractor/<idObjetos>')
def borrarTractor(idObjetos):
    if session.get("loginCorrecto"):
        misTracores.borrar(idObjetos)
        idobjeto = idObjetos
        creador = session['documento'] 
        movimiento = "BorroTractor"
        misMovimientos.agregar([creador, movimiento, idobjeto])
        return redirect('/tractores')
    else:
        return redirect('/')