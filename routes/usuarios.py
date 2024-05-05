from datetime import datetime
import hashlib
from flask import redirect, render_template, request, session
from conexion import *
from models.usuarios import misUsuarios
from models.novedades import misNovedades
from models.servicios import misServicios

# Interfaz para registrar usuarios
@app.route('/registrar')
def registrar():    
    session["logueado"] = False
    fichas = misUsuarios.buscarFicha()
    vFicha = [ficha[0] for ficha in fichas ]
    return render_template("registrar.html", fichas=vFicha)

# Función para guardar usuarios
@app.route("/guardarUsarios", methods=['POST'])
def guardarUsuarios():
    if session.get("loginCorrecto"):
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
            misUsuarios.agregar([documento, nombre, apellido, celular, cifrada, rol, ficha, fecha])
            return redirect('/')
    else:
        return redirect('/')

# Función para el login
@app.route("/login", methods=['POST'])
def login():
    documento = request.form['documento']
    contrasena = request.form['contrasena']
    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
    sql = f"SELECT documento, nombre, apellido, rol FROM usuarios WHERE documento='{documento}' AND contrasena='{cifrada}' AND activo='1'"
    cur = conexion.cursor()
    cur.execute(sql)
    resultado = cur.fetchone()
    if resultado is None:
        return render_template("index.html", msg="Credenciales incorrectas o usuario inactivo")
    else:
        documento = resultado[0]
        nombre = resultado[1]
        apellido = resultado[2]
        rol = resultado[3]
        nombre_completo = f"{nombre} {apellido}"
        session['loginCorrecto'] = True
        session['documento'] = documento
        session['nombreUsuario'] = nombre_completo
        session['rol'] = rol
        return redirect("/Correcto")

# Página de inicio después del login
@app.route('/Correcto')
def redireccion():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return render_template('usuarios/principalUsu.html')
        elif rol == 'Admin' or rol == 'Practicante':
            usuarios = misUsuarios.consultAcepta()
            tractores = misServicios.consultarSolicitadosTractor()
            herramientas = misServicios.consultarSolicitadosHerramienta()
            consumibles = misServicios.consultarSolicitadosConsumible()
            return render_template('lideres/principalLIde.html', usu=usuarios, con=consumibles, her=herramientas, trac=tractores)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# Aceptar usuario
@app.route('/aceptarUsu/<documento_parm>')
def aceptarUsu(documento_parm):
    if session.get("loginCorrecto"):
        misUsuarios.aceptarSi(documento_parm)
        return redirect('/Correcto')
    else:
        return redirect('/')

# Interfaz para aceptar usuarios
@app.route('/aceptarUsuarios')
def aceptarUsuario():
    if session.get("loginCorrecto"):
        rol = session['rol']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/Correcto')
        elif rol == 'Admin' or rol == 'Practicante':
            usuarios = misUsuarios.consultAcepta()
            return render_template("lideres/usuariosAcep.html", usu=usuarios)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')

# Interfaz del perfil propio
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

# Perfil de usuario
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

# Mostrar usuarios activos
@app.route('/usuarios')
def clientes():
    if session.get("loginCorrecto"):
        resultado = misUsuarios.consultar()
        return render_template("usuarios.html", res=resultado)
    else:
        return redirect('/')

# Interfaz de usuarios normales 
@app.route("/principalusuarios")
def usuarios():
    if session.get("loginCorrecto"):
        return render_template('usuarios/principalUsu.html')
    else:
        return redirect('/')
