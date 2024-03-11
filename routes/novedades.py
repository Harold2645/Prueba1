from conexion import *
import datetime
from flask import redirect, render_template, request
from models.novedades import misNovedades


@app.route("/agregarnovedad")
def agregarnovedad():
    return render_template('lideres/novedades/novedadesAg.html')

@app.route("/guardarnovedad", methods=['POST'])
def guardarnovedad():
    idobjeto = request.form['objetotxt']
    documento = request.form['identxt']
    tipo = request.form['tipotxt']
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    descripcion = request.form['destxt']
    foto = request.files['fototxt']
    now = datetime.now()
    tiempo = now.strftime("%Y%H%M%S")

    if foto.filename!='':
        nuevoNombreFoto = tiempo+foto.filename
        foto.save("/uploads/"+nuevoNombreFoto)
    misNovedades.agregarNovedad (idobjeto, documento, tipo, fecha, descripcion, nuevoNombreFoto)
    return redirect('/Correcto')