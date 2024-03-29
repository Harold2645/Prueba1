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
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarPrestado()
        return render_template("lideres/prestamos/prestamosPres.html", res=resultado)
    else:
        return redirect('/')
    
#mostrar Todos los pedidos en espera
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarPedidos()
        return render_template("lideres/prestamos/prestamosPed.html", res=resultado)
    else:
        return redirect('/')

#mostrar Todos los pedidos devueltos
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarDevuelto()
        return render_template("lideres/prestamos/prestamosDev.html", res=resultado)
    else:
        return redirect('/')
    
#mostrar Todos los pedido rechazados)
@app.route('/consultarTodosPedidos')
def consultarTodosPedidos():
    if session.get("loginCorrecto"):
        resultado = misServicios.consultarCancelado()
        return render_template("lideres/prestamos/prestamosCan.html", res=resultado)
    else:
        return redirect('/')
    
