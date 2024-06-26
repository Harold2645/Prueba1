from datetime import datetime, timedelta
from conexion import *
from flask import redirect, render_template, request, session
from models.servicios import misServicios


#mostrar Todos los pedidos (Aceptados,en espera, devueltos o rechazados)
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultar()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Todos los prestamos')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
    
#mostrar Todos los pedidos solicitados
@app.route('/consultarSolicitados')
def consultarSolicitados():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultarSolicitados()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Solicitados')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


#mostrar Todos los pedidos Aceptados
@app.route('/consultarAceptado')
def consultarAceptado():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultarAceptado()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Falta entregar')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
#mostrar Todos los pedidos entregados
@app.route('/consultarprestados')
def consultarprestados():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultarPrestado()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Prestados')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#mostrar Todos los pedidos devueltos
@app.route('/consultarDevueltos')
def consultarDevueltos():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultarDevuelto()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Devueltos')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
#mostrar Todos los pedido rechazados
@app.route('/consultarRechazados')
def consultarRechazados():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractores = misServicios.consultarRechazado()
            return render_template("lideres/prestamos/prestamos.html", trac=tractores, titulo='Rechazados')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    

#Pedir algun objeto
@app.route('/pedir/<idobjeto>')
def pedir(idobjeto):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador' or rol == 'Admin' or rol == 'Practicante':
            hoy = datetime.today()
            hoyDos = hoy + timedelta(days=2)
            hoySemana = hoy + timedelta(days=9)
            minformateada = hoyDos.strftime('%Y-%m-%d')
            maxformateada = hoySemana.strftime('%Y-%m-%d')

            if misServicios.buscarTractor(idobjeto):
                resultado = misServicios.buscarTractor(idobjeto)
                return render_template("pedir.html", res=resultado[0], tipo='Tractor', min=minformateada, max=maxformateada)
            elif misServicios.buscarInsumo(idobjeto):
                resultado = misServicios.buscarInsumo(idobjeto)
                return render_template("pedir.html", res=resultado[0], tipo='Insumo', min=minformateada, max=maxformateada)
            elif misServicios.buscarLiquido(idobjeto):
                resultado = misServicios.buscarLiquido(idobjeto)
                return render_template("pedir.html", res=resultado[0], tipo='Liquido', min=minformateada, max=maxformateada)
            elif misServicios.buscarHerramienta(idobjeto):
                resultado = misServicios.buscarHerramienta(idobjeto)
                return render_template("pedir.html", res=resultado[0], tipo='Herramienta', min=minformateada, max=maxformateada)
            else:
                return redirect('/')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/devolver/<idservicio>')
def devolver(idservicio):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/devoluciones/devoluciones.html", idservicio=idservicio)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
#Form de pedido
@app.route('/devolucion', methods=['POST'])
def devolucion():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            id = request.form['idservicio']
            descripcion = request.form['descripcion']
            foto = request.files['foto']
            hora = datetime.now()
            fnombre,fextension = os.path.splitext(foto.filename)  
            fotot = "D"+hora.strftime("%Y%m%d%H%M%S")+fextension        
            foto.save("uploads/" + fotot)
            envio=[id,hora,descripcion,fotot]
            misServicios.devuelto(envio)
            return redirect("/Correcto")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/prestado/<idservicio>')
def prestado(idservicio):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/prestamos/prestar.html", idservicio=idservicio)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#Form de pedido
@app.route('/pedido', methods=['POST'])
def pedido():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            id = request.form['idservicio']
            estadosalida = request.form['estado']
            encargado = session['documento']
            envio=[id,estadosalida,encargado]
            misServicios.prestado(envio)
            return redirect("/Correcto")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#Form de prestamo
@app.route('/prestamo', methods=['POST'])
def prestamo():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador' or rol == 'Admin' or rol == 'Practicante':
            idobjeto = request.form['idobjeto']
            labor = request.form['labor']
            documento = session['documento']
            if 'ficha' in request.form and len(request.form['ficha']) > 0:
                ficha = request.form['ficha']
            else:
                ficha = '0'
            fecha = request.form['fecha']
            if 'cantidad' in request.form and len(request.form['cantidad']) > 0:
                cantidad = request.form['cantidad']
            else:
                cantidad = '1'
            tipo = request.form['tipo']
            agg=[idobjeto,labor,documento,ficha,fecha,cantidad,tipo]
            misServicios.pedir(agg)
            return redirect("/Correcto")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


#Aceptar pedido 
@app.route('/aceptarPedido/<id>')
def aceptarPedido(id):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            misServicios.aceptarPrestamo(id)
            return redirect('/Correcto')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#Pedido devuelto pedido 
@app.route('/rechazar/<id>')
def rechazar(id):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            misServicios.rechazarPrestamo(id)
            return redirect('/Correcto')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    

@app.route('/mispedidos')
def mispedidos():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador' or rol == 'Admin' or rol == 'Practicante':
            id = session['documento']
            tractores = misServicios.consultarMios(id)
            return render_template("usuarios/pedidos.html",trac=tractores, titulo='Mis pedidos')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/vermasServicios/<id>')
def vermasServicios(id):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscar(id)
            print(resultado)
            return render_template('lideres/prestamos/verMas.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

