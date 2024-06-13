from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.tractores import misTracores
from models.movimientos import misMovimientos
from models.hojaClas import misFichas
from models.servicios import misServicios



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
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misTracores.todoslosTractores()
            return render_template("lideres/tractores/verTractores.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#agregar tractores
@app.route("/agregarTractor")
def agregaarticulo():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            categorias = misCategorias.categoriasTractor()
            return render_template("lideres/tractores/tractoresAg.html", categorias=categorias)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarTractor",   methods=['POST'])
def agregarTrac():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            creador = session['documento'] 
            idobjeto = request.form['idobjeto']
            categoria = request.form['idcategoria']
            foto = request.files['fototrac']
            hora = datetime.now()
            fechacreacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            marca = request.form['marca']
            modelo = request.form['modelo']
            fechamodelo = request.form['fechamodelo']
            if misTracores.buscar(idobjeto):
                categorias = misCategorias.categoriasTractor()
                return render_template("lideres/tractores/tractoresAg.html", categorias=categorias, msg="Id ya existente")
            else:
                fnombre,fextension = os.path.splitext(foto.filename)  
                fotot = "T"+hora.strftime("%Y%m%d%H%M%S")+fextension        
                foto.save("uploads/" + fotot)
                misTracores.agregar([idobjeto, categoria, fotot, fechacreacion, creador,marca, modelo,fechamodelo])
                        #funcion de guardar en tabla movimientos
                movimiento = "AgregoTractor"
                misMovimientos.agregar([creador, movimiento, idobjeto])
                return redirect("/tractores")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


#editar tractores
@app.route('/editarTractor/<idObjeto>')
def editarTractor(idObjeto):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            tractor = misTracores.buscar(idObjeto)
            categorias = misCategorias.categoriasTractor()
            return render_template("lideres/tractores/tractoresEd.html",tractor=tractor[0], categorias=categorias)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/actualizarTractor', methods=['POST'])
def actualizarTractor():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idobjeto = request.form['id_tractor']
            categoria = request.form['id_categoria']
            marca = request.form['marca']
            modelo = request.form['modelo']
            foto = request.files['fototrac']
            fechamodelo = request.form['fechamodelo']
            activo = request.form['activo']
            if foto.filename == '':
                foto1 = request.form['foto1']
                misTracores.modificar([idobjeto, categoria, foto1, marca, modelo, fechamodelo,activo])
            else:
                hora = datetime.now()
                fnombre,fextension = os.path.splitext(foto.filename)  
                fotot = "T"+hora.strftime("%Y%m%d%H%M%S")+fextension        
                foto.save("uploads/" + fotot)
                misTracores.modificar([idobjeto, categoria, fotot, marca, modelo, fechamodelo,activo])

            creador = session['documento'] 
            movimiento = "EditoTractor"
            misMovimientos.agregar([creador, movimiento, idobjeto])
            return redirect("/consultarTractores")
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#borrar tractores 
@app.route('/borrarTractor/<idObjetos>')
def borrarTractor(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            misTracores.borrar(idObjetos)
            idobjeto = idObjetos
            creador = session['documento'] 
            movimiento = "BorroTractor"
            misMovimientos.agregar([creador, movimiento, idobjeto])
            return redirect('/tractores')
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#hoja de vida del tractor 

@app.route('/hojavidatractores/<idObjetos>')
def tractor(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misFichas.consultarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractores.html",res=resultado, trac=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/agregar/<idObjetos>")
def agregar(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template('lideres/hojaVida/tractorAG.html', res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/agregarHoja", methods=['POST'])
def agregarA():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idObjetos = request.form['idObjetos']
            nodstractor = request.form['nodstractor']
            nosmotor = request.form['nosmotor']
            potenciadmotor = request.form['potenciadmotor']
            pasodtractor = request.form['pasodtractor']
            numerodcilindro = request.form['numerodcilindro']
            tipodmotorlv = request.form['tipodmotorlv']
            numerodcha = request.form['numerodcha']
            numerodcer = request.form['numerodcer']

            misFichas.agregarA([idObjetos,nodstractor, nosmotor, potenciadmotor, pasodtractor, numerodcilindro,tipodmotorlv,numerodcha,numerodcer])
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractorBG.html", res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/agregarBG/<idObjetos>')
def agregarBG(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template('lideres/hojaVida/tractorBG.html', res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/agregarHojaB', methods=['POST'])
def agregarB():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idObjetos = request.form['idObjetos']
            tipodtraccion = request.form["tipodtraccion"]
            distanciaeejes = request.form["distanciaeejes"]
            alturadpacded = request.form["alturadpacded"]
            alturatotal = request.form["alturatotal"]
            alturadetatdlc = request.form["alturadetatdlc"]
            alturamlb = request.form["alturamlb"]
            longitudtilbdt = request.form["longitudtilbdt"]
            anchototalf = request.form["anchototalf"]
            anchototalg = request.form["anchototalg"]
            alturadpaddl = request.form["alturadpaddl"]
            alturadpadtn = request.form["alturadpadtn"]
            distanciadpato = request.form["distanciadpato"]
            tomafnde = request.form["tomafnde"]
            tomafrtrm = request.form["tomafrtrm"]
            agr = [idObjetos,tipodtraccion,distanciaeejes,alturadpacded,alturatotal,alturadetatdlc,alturamlb,longitudtilbdt,anchototalf,anchototalg,alturadpaddl,alturadpadtn,distanciadpato,tomafnde,tomafrtrm]
            misFichas.agregarB(agr)
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractorCG.html", res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')



@app.route('/agregarCG/<idObjetos>')
def agregarCG(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template('lideres/hojaVida/tractorCG.html', res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/agregarHojaC', methods=['POST'])
def agregarC():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idObjetos = request.form['idObjetos']
            tipodidcncr = request.form["tipodidcncr"]
            marcadlbdi = request.form["marcadlbdi"]
            referenciadlbdin = request.form["referenciadlbdin"]
            tensionesdlltsr = request.form["tensionesdlltsr"]
            tencionmdllt = request.form["tencionmdllt"]
            cargampslrt = request.form["cargampslrt"]
            desgastedlrt = request.form["desgastedlrt"]
            dimesionesdlldsr = request.form["dimesionesdlldsr"]
            presionmdlld = request.form["presionmdlld"]
            cargampslrd = request.form["cargampslrd"]
            desgastesdlrd  = request.form["desgastesdlrd"]
            agr  = [idObjetos,tipodidcncr,marcadlbdi,referenciadlbdin,tensionesdlltsr,tencionmdllt,cargampslrt,desgastedlrt,dimesionesdlldsr,presionmdlld,cargampslrd,desgastesdlrd]
            misFichas.agregarC(agr)
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractorDG.html", res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')



@app.route('/agregarDG/<idObjetos>')
def agregarDG(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template('lideres/hojaVida/tractorDG.html', res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/agregarHojaD', methods=['POST'])
def agregarD():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idObjetos = request.form['idObjetos']
            aceitemotor = request.form["aceitemotor"]
            aceitehidraulico = request.form["aceitehidraulico"]
            aceitetransmision = request.form["aceitetransmision"]
            aceiteddd = request.form["aceiteddd"]
            aceiteldf = request.form["aceiteldf"]
            filtrodammr = request.form["filtrodammr"]
            filtrodcmr = request.form["filtrodcmr"]
            filtrodahmr = request.form["filtrodahmr"]
            filtrodapmr = request.form["filtrodapmr"]
            filtrodasmr = request.form["filtrodasmr"]
            bateriamr = request.form["bateriamr"]
            numerodpelrta = request.form["numerodpelrta"]
            numerodpelrt = request.form["numerodpelrt"]
            
            misFichas.agregarD([idObjetos,aceitemotor,aceitehidraulico,aceitetransmision,aceiteddd,aceiteldf,filtrodammr,filtrodcmr,filtrodahmr,filtrodapmr,filtrodasmr,bateriamr,numerodpelrta,numerodpelrt])
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractorEG.html", res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


@app.route('/agregarEG/<idObjetos>')
def agregarEG(idObjetos):
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misServicios.buscarTractor(idObjetos)
            return render_template('lideres/hojaVida/tractoreG.html', res=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route('/agregarHojaE', methods=['POST'])
def agregarE():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            idObjetos = request.form['idObjetos']
            ftdrenaje = request.files["ftdrenaje"]
            hora = datetime.now()
            fnombre,fextension = os.path.splitext(ftdrenaje.filename)
            ftdrenajea = "FD"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftdrenaje.save("uploads/" + ftdrenajea)

            ftbateria = request.files["ftbateria"]
            fnombre,fextension = os.path.splitext(ftbateria.filename)
            ftbateriaa = "FB"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftbateria.save("uploads/" + ftbateriaa)

            ftfiltroac = request.files["ftfiltroac"]
            fnombre,fextension = os.path.splitext(ftfiltroac.filename)
            ftfiltroaca = "FFA"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftfiltroac.save("uploads/" + ftfiltroaca)

            ftfiltroar = request.files["ftfiltroar"]
            fnombre,fextension = os.path.splitext(ftfiltroar.filename)
            ftfiltroara = "FFB"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftfiltroar.save("uploads/" + ftfiltroara)

            ftfiltroachid = request.files["ftfiltroachid"]
            
            fnombre,fextension = os.path.splitext(ftfiltroachid.filename)
            ftfiltroachida = "FFC"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftfiltroachid.save("uploads/" + ftfiltroachida)

            ftfiltrocomb = request.files["ftfiltrocomb"]
            
            fnombre,fextension = os.path.splitext(ftfiltrocomb.filename)
            ftfiltrocomba = "FFCB"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftfiltrocomb.save("uploads/" + ftfiltrocomba)

            ftcabeza = request.files["ftcabeza"]
            
            fnombre,fextension = os.path.splitext(ftcabeza.filename)
            ftcabezaa = "FC"+hora.strftime("%Y%m%d%H%M%S")+fextension
            ftcabeza.save("uploads/" + ftcabezaa)

            fotos=[idObjetos,ftdrenajea,ftbateriaa,ftfiltroaca ,ftfiltroara ,ftfiltroachida ,ftfiltrocomba ,ftcabezaa]

            misFichas.agregarE(fotos)
                
            resultado = misFichas.consultarTractor(idObjetos)
            return render_template("lideres/hojaVida/tractores.html",res=resultado, trac=resultado[0])
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')