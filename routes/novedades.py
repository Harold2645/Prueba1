from conexion import *
import datetime
from flask import redirect, render_template, request, session
from models.novedades import misNovedades
from models.usuarios import misUsuarios

@app.route("/agregarnovedad")
def agregarnovedad():
    if session.get("loginCorrecto"):
        return render_template('lideres/novedades/novedadesAg.html')
    else:
        return redirect('/')

@app.route("/guardarnovedad", methods=['POST'])
def guardarnovedad():
    if session.get("loginCorrecto"):
        idobjeto = request.form['objetotxt']
        documento = request.form['identxt']
        tipo = request.form['tipotxt']
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descripcion = request.form['destxt']
        foto = request.files['fototxt']
        now = datetime.datetime.now()
        tiempo = now.strftime("%Y%H%M%S")
        nuevoNombreFoto = ""

        if foto.filename != '':
            nuevoNombreFoto = tiempo + foto.filename
            foto.save("uploads/" + nuevoNombreFoto)

        misNovedades.agregarNovedad(idobjeto, documento, tipo, fecha, descripcion, nuevoNombreFoto)
        return redirect('/Correcto')
    else:
        return redirect('/')

@app.route('/novedades')
def novedades():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misNovedades.consultarNovedades()
            return render_template('lideres/novedades/novedades.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
