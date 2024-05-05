from datetime import datetime
from conexion import *
from flask import redirect, render_template, request, session
from models.servicios import misServicios


#mostrar Todos los pedidos (Aceptados,en espera, devueltos o rechazados)
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarTractor()
        herramientas = misServicios.consultarHerramienta()
        consumibles = misServicios.consultarConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Todos los prestamos')
    else:
        return redirect('/')
    
    
#mostrar Todos los pedidos solicitados
@app.route('/consultarSolicitados')
def consultarSolicitados():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarSolicitadosTractor()
        herramientas = misServicios.consultarSolicitadosHerramienta()
        consumibles = misServicios.consultarSolicitadosConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Solicitados')
    else:
        return redirect('/')


#mostrar Todos los pedidos Aceptados
@app.route('/consultarAceptado')
def consultarAceptado():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarAceptadoTractor()
        herramientas = misServicios.consultarAceptadoHerramienta()
        consumibles = misServicios.consultarAceptadoConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Falta entregar')
    else:
        return redirect('/')
    
#mostrar Todos los pedidos entregados
@app.route('/consultarprestados')
def consultarprestados():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarPrestadoTracor()
        herramientas = misServicios.consultarPrestadoHerramienta()
        consumibles = misServicios.consultarPrestadoConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Prestados')
    else:
        return redirect('/')

#mostrar Todos los pedidos devueltos
@app.route('/consultarDevueltos')
def consultarDevueltos():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarDevueltoTractor()
        herramientas = misServicios.consultarDevueltoHerramienta()
        consumibles = misServicios.consultarDevueltoConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Devueltos')
    else:
        return redirect('/')
    
#mostrar Todos los pedido rechazados
@app.route('/consultarRechazados')
def consultarRechazados():
    if session.get("loginCorrecto"):
        tractores = misServicios.consultarRechazadoTractor()
        herramientas = misServicios.consultarRechazadoHerramienta()
        consumibles = misServicios.consultarRechazadoConsumible()
        return render_template("lideres/prestamos/prestamos.html",con=consumibles , her=herramientas , trac=tractores, titulo='Rechazados')
    else:
        return redirect('/')
    

#Pedir algun objeto
@app.route('/pedir/<idobjeto>')
def pedir(idobjeto):
    if session.get("loginCorrecto"):
        if misServicios.buscarTractor(idobjeto):
            resultado = misServicios.buscarTractor(idobjeto)
            return render_template("pedir.html", res=resultado[0], tipo='Tractor')
        elif misServicios.buscarInsumo(idobjeto):
            resultado = misServicios.buscarInsumo(idobjeto)
            return render_template("pedir.html", res=resultado[0], tipo='Insumo')
        elif misServicios.buscarHerramienta(idobjeto):
            resultado = misServicios.buscarHerramienta(idobjeto)
            return render_template("pedir.html", res=resultado[0], tipo='Herramienta')
        else:
            return redirect('/')
    else:
        return redirect('/')
    
@app.route('/devolver/<idservicio>')
def devolver(idservicio):
    if session.get("loginCorrecto"):
        return render_template("lideres/devoluciones/devoluciones.html", idservicio=idservicio)
    else:
        return redirect('/')
    
#Form de pedido
@app.route('/devolucion', methods=['POST'])
def devolucion():
    id = request.form['idservicio']
    print(id)
    descripcion = request.form['descripcion']
    foto = request.files['foto']

    hora = datetime.now()
    fnombre,fextension = os.path.splitext(foto.filename)  
    fotot = "D"+hora.strftime("%Y%m%d%H%M%S")+fextension        
    foto.save("uploads/" + fotot)

    envio=[id,hora,descripcion,fotot]
    misServicios.devuelto(envio)

    return redirect("/Correcto")

@app.route('/prestado/<idservicio>')
def prestado(idservicio):
    if session.get("loginCorrecto"):
        return render_template("lideres/prestamos/prestar.html", idservicio=idservicio)
    else:
        return redirect('/')

#Form de pedido
@app.route('/pedido', methods=['POST'])
def pedido():
    id = request.form['idservicio']
    estadosalida = request.form['estado']
    encargado = session['documento']
    envio=[id,estadosalida,encargado]
    print(envio)
    misServicios.prestado(envio)

    return redirect("/Correcto")


#Form de prestamo
@app.route('/prestamo', methods=['POST'])
def prestamo():
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


#Aceptar pedido 
@app.route('/aceptarPedido/<id>')
def aceptarPedido(id):
    misServicios.aceptarPrestamo(id)
    return redirect('/Correcto')


#pedido  Prestado
# @app.route('/prestado/<id>')
# def prestado(id):
#     misServicios.prestado(id)
#     return redirect('/Correcto')

#Pedido devuelto pedido 
# @app.route('/devolver/<id>')
# def devolver(id):
#     misServicios.devuelto(id)
#     return redirect('/Correcto')

#Pedido devuelto pedido 
@app.route('/rechazar/<id>')
def rechazar(id):
    misServicios.rechazarPrestamo(id)
    return redirect('/Correcto')