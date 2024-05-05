from conexion import *
from datetime import datetime
from flask import redirect, render_template, request, session
from models.categorias import misCategorias
from models.liquidos import misLiquidos
from models.movimientos import misMovimientos

# Liquidos

# mostrar Liquidos
@app.route('/consultarLiquidos')
def consultaLiquidos():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect ('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misLiquidos.consultarliquidos()
            return render_template("lideres/liquidos/liquidos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
@app.route('/consultarlosLiquidos')
def consultalarLiquidos():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misLiquidos.todoslosliquidos()
            return render_template("lideres/liquidos/verLiquidos.html", res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# agregar Liquidos
@app.route("/agregarLiquidos")
def agregarLiquidos():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            categorias = misCategorias.categoriasInsumos()
            return render_template("lideres/liquidos/liquidosAg.html", categorias=categorias)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

@app.route("/guardarLiquidos" ,methods=['POST'])
def guardarLiquidos():
    if session.get("loginCorrecto"):
        documento = session['documento'] 
        idCategoria = request.form.get('id_categoria')
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        foto = request.files['foto']
        ahora = datetime.now()
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        creador = documento
        fnombre,fextension = os.path.splitext(foto.filename)
        nombreFoto = "L"+ahora.strftime("%Y%m%d%H%M%S")+fextension
        foto.save("uploads/"+nombreFoto)
        misLiquidos.agregar([idCategoria,nombre,cantidad,nombreFoto,fecha,creador])

        movimiento = "AgregoLiquido"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect("/consultarLiquidos")
    else:
        return redirect('/')

# borrar Liquidos 
@app.route('/borrarLiquidos/<idObjetos>')
def borrarLiquidos(idObjetos):
    if session.get("loginCorrecto"):
        misLiquidos.borrar(idObjetos)

        nombre = misLiquidos.buscarnombre(idObjetos)
        creador = session['documento'] 
        movimiento = "BorroLiquido"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect('/consultarLiquidos')
    else:
        return redirect('/')

# editar Liquidos
@app.route('/editarLiquidos/<idObjeto>')
def editarLiquidos(idObjeto):
    if session.get("loginCorrecto"):
        Consu = misLiquidos.buscar(idObjeto)
        categorias = misCategorias.categoriasLiquidos()
        return render_template("Liquidos/modificarLiquidos.html",Consu=Consu[0], categorias=categorias)
    else:
        return redirect('/')
    
@app.route('/actualizarLiquidos', methods=['POST'])
def actualizarLiquidos():
    if session.get("loginCorrecto"):
        idObjeto = request.form['id_Consumible']
        nombre = request.form['nombre']
        categoria = request.form.get('id_categoria')
        estado = request.form['estado']
        disponibilidad = request.form['disponibilidad']
        activo = request.form['activo']
        modif = [idObjeto,nombre,categoria,estado,disponibilidad,activo]
        misLiquidos.modificar(modif)

        creador = session['documento'] 
        movimiento = "EditoLiquido"
        misMovimientos.agregar([creador, movimiento, nombre])
        return redirect("/consultarLiquidos")
    else:
        return redirect('/')
