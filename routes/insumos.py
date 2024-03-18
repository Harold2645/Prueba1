from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.insumos import misInsumos


#Consumibles

#mostrar consumibles
@app.route('/consultarConsumibles')
def consultaConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        resultado = misInsumos.consultarinsumos()
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/insumos.html', res=resultado)
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template("lideres/insumos/insumos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/consultarlosConsumibles')
def consultalarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misInsumos.todoslosinsumos()
            return render_template("lideres/insumos/verInsumos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

#agregar Consumibles
@app.route("/agregarConsumibles")
def agregarConsumibles():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            categorias = misCategorias.categoriasInsumos()
            return render_template("lideres/insumos/insumosAg.html", categorias=categorias)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarConsumibles" ,methods=['POST'])
def guardarConsumibles():
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
    print(idCategoria,nombre,cantidad,nombreFoto,fecha,creador)
    return redirect("/consultarConsumibles")

#borrar Consumibles 
@app.route('/borrarConsumibles/<idObjetos>')
def borrarConsumibles(idObjetos):
    misInsumos.borrar(idObjetos)
    return redirect('/consultarConsumibles')



#Falta organizar




#editar Consumibles
@app.route('/editarConsumibles/<idObjeto>')
def editarConsumibles(idObjeto):
    if session.get("loginCorrecto"):
        Consu = misInsumos.buscar(idObjeto)
        categorias = misCategorias.categoriasConsumibles()
        return render_template("consumibles/modificarConsumibles.html",Consu=Consu[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarConsumibles', methods=['POST'])
def actualizarConsumibles():
    idObjeto = request.form['id_Consumible']
    nombre = request.form['nombre']
    categoria = request.form.get('id_categoria')
    estado = request.form['estado']
    disponibilidad = request.form['disponibilidad']
    activo = request.form['activo']
    modif = [idObjeto,nombre,categoria,estado,disponibilidad,activo]
    misInsumos.modificar(modif)
    return redirect("/consultarConsumibles")