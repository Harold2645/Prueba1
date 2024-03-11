from datetime import datetime
import hashlib
from flask import redirect, render_template, request, session
from conexion import *
from models.usuarios import misUsuarios
from models.inventario import misTracores
from models.novedades import misNovedades


#Interfaz registrar usuarios
@app.route('/registrar')
def registrar():
    fichas = misUsuarios.buscarFicha()
    return render_template("registrar.html",fichas=fichas)

# Funcion Guardar Usuarios
@app.route("/guardarUsarios", methods=['POST'])
def guardarUsuarios():
    documento = request.form['documento']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    celular = request.form['celular']
    contrasena = request.form['contrasena']
    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
    rol = request.form['rol']
    ficha = request.form['ficha']
    ahora = datetime.now()
    fecha = ahora.strftime("%Y%m%d%H%M%S")
    existente = misUsuarios.buscar(documento)
    if existente:
        return render_template("registrar.html", msg="Documento ya existe")
    else:
        misUsuarios.agregar([documento,nombre,apellido,celular,cifrada,rol,ficha,fecha])
        return redirect('/')

#Funcion Login
@app.route("/login", methods=['POST'])
def login():
    documento = request.form['documento']
    contrasena = request.form['contrasena']
    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
    cur = mysql.cursor(dictionary=True)
    sql = f"SELECT documento, nombre, apellido, rol FROM usuarios WHERE documento='{documento}' AND contrasena='{cifrada}'"
    cur.execute(sql)
    resultado = cur.fetchone()

    if resultado is None:
        return render_template("index.html", msg="Credenciales incorrectas o usuario inactivo")
    else:
        print(resultado)
        documento = resultado['documento']
        nombre = resultado['nombre']
        apellido = resultado['apellido']
        rol = resultado['rol']
        nombre_completo = f"{nombre} {apellido}"
        session['loginCorrecto'] = True
        session['documento'] = documento
        session['nombreUsuario'] = nombre_completo
        session['rol'] = rol
        return redirect("/Correcto")
    
#Login correcto 
@app.route('/Correcto')
def redireccion():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            resultado = misTracores.consultarTractor()
            return render_template('usuarios/tractores.html', res=resultado)
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misNovedades.consultar()
            return render_template('lideres/novedades/novedades.html', res=resultado)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    
#Interfaz Perfil
@app.route('/perfilPropio')
def perfil():
        if session.get("loginCorrecto"):
            documento = session['documento']
            if misUsuarios.buscar(documento):
                    resultado1 = misUsuarios.buscar(documento)
                    return render_template("perfil.html", res=resultado1)
            else:
                return redirect('/login')
        else:
            return redirect('/')