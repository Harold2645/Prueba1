from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.novedades import misNovedades
from models.servicios import misServicios

@app.route("/agregarnovedad/<idObjeto>")
def agregarnovedad(idObjeto):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            if (misServicios.buscarTractor(idObjeto)):
                return render_template('lideres/novedades/novedadesAg.html', id=idObjeto, tipo="Tractor")
            elif(misServicios.buscarHerramienta(idObjeto)):
                return render_template('lideres/novedades/novedadesAg.html', id=idObjeto, tipo="Herramienta")
            elif(misServicios.buscarInsumo(idObjeto)):
                return render_template('lideres/novedades/novedadesAg.html', id=idObjeto, tipo="Insumo")
            elif(misServicios.buscarLiquido(idObjeto)):
                return render_template('lideres/novedades/novedadesAg.html', id=idObjeto, tipo="Liquido")
            else:
                return redirect ('/panel')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarnovedad", methods=['POST'])
def guardarnovedad():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            idobjeto = request.form['idobjeto']
            documento = session['documento']
            tipo = request.form['tipo']
            hora = datetime.now()
            fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            descripcion = request.form['descripcion']  
            foto = request.files['foto']
            fnombre,fextension = os.path.splitext(foto.filename)  
            fotot = "T"+hora.strftime("%Y%m%d%H%M%S")+fextension        
            foto.save("uploads/" + fotot)

            misNovedades.agregarNovedad([idobjeto, documento, tipo, fecha, descripcion, fotot])
            return redirect('/panel')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/novedades')
def novedades():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misNovedades.consultarNovedades()
            return render_template('lideres/novedades/novedades.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/vermasNovedades/<id>')
def vermasNovedades(id):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misNovedades.buscar(id)
            return render_template('lideres/novedades/verMas.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

