from datetime import datetime
import hashlib
from flask import redirect, render_template, request, session
from conexion import *
from models.usuarios import misUsuarios
from models.novedades import misNovedades
# from models.funciones import misPrestamos


#Interfaz registrar usuarios
@app.route('/registrar')
def registrar():    
    session["logueado"] = False
    fichas = misUsuarios.buscarFicha()
    vFicha = [ficha[0] for ficha in fichas ]
    return render_template("registrar.html",fichas=vFicha)

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
    cur = conexion.cursor(dictionary=True)
    sql = f"SELECT documento, nombre, apellido, rol FROM usuarios WHERE documento='{documento}' AND contrasena='{cifrada}' AND activo='1'"
    cur.execute(sql)
    resultado = cur.fetchone()
    if resultado is None:
        return render_template("index.html", msg="Credenciales incorrectas o usuario inactivo")
    else:
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
            return render_template('usuarios/principalUsu.html')
        elif rol == 'Admin' or rol == 'Practicante':
            resultado = misNovedades.consultarNovedades()
            usuarios = misUsuarios.consultAcepta()
            # prestamos= misPrestamos.consultar()
            return render_template('lideres/principalLIde.html', res=resultado, usu=usuarios)
        # ,pres=prestamos
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')
    

#Aceptar usuario
@app.route('/aceptar/<documento_parm>')
def aceptar(documento_parm):
    misUsuarios.aceptarSi(documento_parm)
    return redirect('/Correcto')

#Interfaz solo para aceptar Usuarios
@app.route('/aceptarUsuarios')
def aceptarUsuario():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect ('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            usuarios = misUsuarios.consultAcepta()
            return render_template("lideres/usuariosAcep.html", usu=usuarios)
        else:
                return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


#Interfaz Perfil
@app.route('/perfilPropio')
def perfilpropio():
    if session.get("loginCorrecto"):
        documento = session['documento']
        if misUsuarios.buscar(documento):
                resultado1 = misUsuarios.buscar(documento)
                return render_template("perfil.html", res=resultado1)
        else:
            return redirect('/login')
    else:
        return redirect('/')
        
#Perfil
@app.route('/perfil/<documento_parm>')
def perfil(documento_parm):
    if session.get("loginCorrecto"):
        rol = session.get('rol')
        if rol == 'Admin':
            if misUsuarios.buscar(documento_parm):
                    resultado1 = misUsuarios.buscar(documento_parm)
                    return render_template("perfil.html", res=resultado1)
            else:
                return redirect('/')
        else:
            documento = session['documento']
            if misUsuarios.buscar(documento):
                    resultado1 = misUsuarios.buscar(documento)
                    return render_template("perfil.html", res=resultado1)
            else:
                return redirect('/')
    else:
            return redirect('/')
    

#mostar usuarios de la base de datos que estan activos
@app.route('/usuarios')
def clientes():
    if session.get("loginCorrecto"):
        resultado = misUsuarios.consultar()
        return render_template("usuarios.html", res=resultado)
    else:
        return redirect('/')
    

#Interfaz de usuarios normales 
@app.route("/principalusuarios")
def usuarios():
    if session.get("loginCorrecto"):
        return render_template('usuarios/principalUsu.html')
    else:
            return redirect('/')