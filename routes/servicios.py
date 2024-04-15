from datetime import datetime
from conexion import *
from flask import redirect, render_template, request, session
from models.servicios import misServicios


#mostrar Todos los pedidos (Aceptados,en espera, devueltos o rechazados)
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultar()
        return render_template("lideres/prestamos/prestamos.html", res=resultado)
    else:
        return redirect('/')

#mostrar Todos los pedidos Aceptados
@app.route('/consultarPorEntregar')
def consultarPorEntregar():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarPorEntregar()
        return render_template("lideres/prestamos/prestamosEntre.html", res=resultado)
    else:
        return redirect('/')

#mostrar Todos los pedidos Aceptados
@app.route('/consultarAceptado')
def consultarAceptado():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarPrestado()
        return render_template("lideres/prestamos/prestamosPres.html", res=resultado)
    else:
        return redirect('/')
    
#mostrar Todos los pedidos en espera
@app.route('/consultarEnEspera')
def consultarEnEspera():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarSolicitados()
        return render_template("lideres/prestamos/prestamosPed.html", res=resultado)
    else:
        return redirect('/')

#mostrar Todos los pedidos devueltos
@app.route('/consultarDevueltos')
def consultarDevueltos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarDevuelto()
        return render_template("lideres/prestamos/prestamosDev.html", res=resultado)
    else:
        return redirect('/')
    
#mostrar Todos los pedido rechazados
@app.route('/consultarRechazados')
def consultarRechazados():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarRechazado()
        return render_template("lideres/prestamos/prestamosCan.html", res=resultado)
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

@app.route('/aceptarPedido/<id>')
def aceptarPedido(id):
    misServicios.aceptarPrestamo(id)
    return redirect('/Correcto')

