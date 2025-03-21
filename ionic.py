import base64
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from conexion import *
import hashlib
from datetime import datetime
from flask import jsonify, request
import os


@app.route('/loginIonicA', methods=['POST'])
def loginIonicA():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cifrada = hashlib.sha512(data['contrasena'].encode("utf-8")).hexdigest()
        cursor.execute(f"SELECT documento, nombre, apellido, rol FROM usuarios WHERE documento='{data['documento']}' AND contrasena='{cifrada}' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/loginIonicB', methods=['POST'])
def loginIonicB():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT documento, nombre, apellido, rol FROM usuarios WHERE documento='{data['documento']}' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultarolIonic', methods=['POST'])
def consultarolIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT rol FROM usuarios WHERE documento='{data['documento']}'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaUsuarioIonic', methods=['GET'])
def consultaUsuarioIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE activo=1")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/registrarUsuarioIonic', methods=['POST'])
def registrarUsuarioIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuario (documento, nombre, apellido, celular) VALUES (%s, %s, %s, %s)", (data['documento'], data['nombre'], data['apellido'], data['celular']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})  
    

@app.route('/consultaTractoresIonic', methods=['GET'])
def consultaTractoresIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = "SELECT tractores.marca, tractores.modelo, tractores.idobjeto, tractores.idcategoria, tractores.fototrac, tractores.activo, categorias.idcategoria, categorias.nombre, categorias.tipo FROM tractores INNER JOIN categorias WHERE tractores.idcategoria = categorias.idcategoria AND tractores.activo = '1' AND categorias.tipo = 'Tractor';"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['fototrac'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['fototrac'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['fototrac'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)

        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
   
@app.route('/consultaLiquidoIonic', methods=['GET'])
def consultaLiquidoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre as nombreC FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Liquido' AND consumibles.activo = '1';"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['foto'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['foto'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['foto'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)

        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/consultaNovedadIonic', methods=['GET'])
def consultaNovedadIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = "SELECT * FROM (SELECT t.marca AS nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM tractores AS t INNER JOIN novedades AS n ON t.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento UNION ALL SELECT h.nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM herramientas AS h INNER JOIN novedades AS n ON h.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento UNION ALL SELECT c.nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM consumibles AS c INNER JOIN novedades AS n ON c.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento) AS combined_results ORDER BY fecha DESC;"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['foto'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['foto'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['foto'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)
        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaHerramientaIonic', methods=['GET'])
def consultaHerramientaIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = "SELECT herramientas.idobjeto, herramientas.nombre, herramientas.foto, categorias.tipo, categorias.descripcion FROM herramientas INNER JOIN categorias ON categorias.idcategoria = herramientas.idcategoria WHERE herramientas.activo='1';"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['foto'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['foto'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['foto'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)

        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/misPedidos/<id>', methods=['GET'])
def misPedidos(id):
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute (f"SELECT * FROM (SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.documento = {id} UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.documento = {id} UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.documento = {id}) AS combined_results ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        if(len(datos)==0):
            cursor.close()
            return jsonify({"msg":"notFound"})
        else:
            cursor.close()
            return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})  
    
@app.route('/agregarHerramientasIonic', methods=['POST'])
def agregarHerramientasIonic():
    try:
        data = request.get_json()

        # Decodificar la imagen de Base64 y guardarla
        if data.get('foto'):
            foto_data = data['foto']
            ahora = datetime.now()
            referencia = "H"+ahora.strftime("%Y%m%d%H%M%S")

            foto_nombre = f"{referencia}.png"  # Puedes cambiar la extensión si es necesario
            foto_path = os.path.join('uploads', foto_nombre)

            # Asegúrate de que la carpeta de destino exista
            os.makedirs('uploads', exist_ok=True)

            # Decodificar y guardar la imagen
            with open(foto_path, "wb") as fh:
                fh.write(base64.b64decode(foto_data.split(',')[1]))

        # Simulación de inserción en la base de datos
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO herramientas (idobjeto, idcategoria, nombre, cantidad, foto, activo, fecha, creador) VALUES (%s, %s, %s, '1', %s, '1', '{fecha}', %s)", 
                    (data['idobjeto'], data['idcategoria'], data['nombre'], foto_nombre, data['creador']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
@app.route('/eliminarHerramientaIonic', methods=['POST'])
def eliminarHerramientaIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("UPDATE herramientas SET  activo = '0' WHERE idobjeto = %s", ([data['idobjeto']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/perfilIonic/<id>', methods=['GET'])
def perfilIonic(id):
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute (f"SELECT * FROM usuarios WHERE documento={id}")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        if(len(datos)==0):
            cursor.close()
            return jsonify({"msg":"notFound"})
        else:
            cursor.close()
            return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})  
    
@app.route('/solicitarIonic', methods=['POST'])
def solicitarIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime("%Y%m%d%H%M%S")
        cursor.execute(f"INSERT INTO servicios (idobjeto, labor, documento, ficha, fechasalida, cantidad, tipo, estado,fechasoli) VALUES (%s, %s, %s, %s,%s, %s, %s,'S','{fecha}')", (data['idobjeto'],data['labor'],data['documento'],data['ficha'],data['fechasalida'],data['cantidad'],data['tipo']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})  

    
@app.route('/registrarIonic', methods=['POST'])
def registrarIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO usuarios (documento,nombre,apellido,celular,contrasena,rol,ficha,fecha,activo) VALUES (%s, %s, %s, %s, %s, %s, %s, '{fecha}','2')", (data['documento'], data['nombre'], data['apellido'], data['celular'], data['contrasena'], data['rol'], data['ficha']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/categoriasTractorIonic', methods=['GET'])
def categoriasTractorIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias WHERE tipo='Tractor' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/agregarTractorIonic', methods=['POST'])
def agregarTractorIonic():
    try:
        data = request.get_json()

        # Decodificar la imagen de Base64 y guardarla
        if data.get('foto'):
            foto_data = data['foto']

            ahora = datetime.now()
            referencia = "T"+ahora.strftime("%Y%m%d%H%M%S")

            foto_nombre = f"{referencia}.png"  # Puedes cambiar la extensión si es necesario
            foto_path = os.path.join('uploads', foto_nombre)

            # Asegúrate de que la carpeta de destino exista
            os.makedirs('uploads', exist_ok=True)

            # Decodificar y guardar la imagen
            with open(foto_path, "wb") as fh:
                fh.write(base64.b64decode(foto_data.split(',')[1]))

        # Simulación de inserción en la base de datos
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO tractores (idobjeto, idcategoria, fototrac, activo, fechacreacion, creador, marca, modelo,fechamodelo) VALUES (%s, %s, %s, '1', '{fecha}', %s, %s, %s, %s)", (data['idobjeto'], data['idcategoria'], foto_nombre, data['creador'], data['marca'], data['modelo'], data['fechamodelo']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
@app.route('/eliminarTractorIonic', methods=['POST'])
def eliminarTractorIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("UPDATE tractores SET activo=0 WHERE idObjeto = %s", ([data['idobjeto']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/editarTractorIonic/<id>', methods=['POST'])
def editarTractorIonic(id):
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM herramientas WHERE idobjeto = {id}")
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/editarHerramientaIonicConsulta/<id>', methods=['GET'])
def editarHerramientaIonicConsulta(id):
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM herramientas WHERE idobjeto = '{id}'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
        print(e)


# // cosas de edinson urbano no tocar por favor
# // cosas de edinson urbano no tocar por favor
@app.route('/datosgrafLiquidosIonic', methods=['GET'])
def datosgrafLiquidosIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT nombre, SUM(cantidad) as cantidad_total FROM consumibles WHERE tipo = 'Liquido' GROUP BY nombre ORDER BY nombre ASC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/datosgrafTractoresIonic', methods=['GET'])
def datosgrafTractoresIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"""
            SELECT 
                tractores.marca, 
                servicios.fechasalida, 
                COUNT(servicios.idobjeto) AS usos 
            FROM 
                servicios 
            INNER JOIN 
                tractores ON tractores.idobjeto = servicios.idobjeto 
            WHERE 
                servicios.tipo = 'Tractor' AND tractores.activo = '1' 
            GROUP BY 
                tractores.marca, servicios.fechasalida 
            ORDER BY 
                servicios.fechasalida;
        """)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/envioConsuPezIonic', methods=['POST'])
def envioConsuPezIonic():
    correoSub = request.json['correo']
    print(f"Correo recibido: {correoSub}")

    remitente = "hangarsencacab@gmail.com"
    destinatario = correoSub
    password = "wvyi ztyc vc fj rspx"  #wvyi ztyc vc fj rspx

    mensaje = """
            <html>
                    <body>
                        <p>Cordial saludo Estimado,</p>
                        <p>Nos dirigimos a usted desde el Centro Agropecuario de Buga SENA CAB, específicamente del equipo encargado del hangar, para informarle que los niveles de combustible diésel disponibles para los tractores están alcanzando sus límites mínimos.</p>
                        <p>Es fundamental para nosotros mantener los tractores operativos para asegurar el correcto funcionamiento de nuestras actividades diarias y cumplir con nuestros objetivos. Por ello, solicitamos de manera urgente el reabastecimiento de combustible diésel.</p>
                        <p>Adjunto encontrará un gráfico que ilustra los niveles actuales de combustible en nuestra bodega.</p>
                        <p>Agradecemos de antemano su pronta atención a esta solicitud y quedamos a la espera de su respuesta.</p>
                        <div style="display: flex; align-items: center">
                            <p><img src="cid:logo_sena" alt="Logo SENA" style=" width: 180px;"></p>
                            <div>
                                <p>Atentamente,</p>
                                <p>Equipo de Gestión del Hangar</p>
                                <p>Centro Agropecuario de Buga SENA CAB</p>
                            </div>
                        </div>
                    </body>
                </html>
            """

    email = MIMEMultipart()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "!!Solicitud Urgente de Reabastecimiento de Combustible Diésel!!"

    email.attach(MIMEText(mensaje, "html"))

    ruta_logo = os.path.join(app.root_path, 'static', 'img', 'logoSena.png')

    with open(ruta_logo, 'rb') as archivo_imagen:
        imagen = MIMEImage(archivo_imagen.read())
        imagen.add_header('Content-ID', '<logo_sena>')
        email.attach(imagen)

    filename = "graficoIonic.pdf"
    with open(filename, "rb") as archivo_grafico:
        adjunto_grafico = MIMEBase("application", "octet-stream")
        adjunto_grafico.set_payload(archivo_grafico.read())
        encoders.encode_base64(adjunto_grafico)
        adjunto_grafico.add_header("Content-Disposition", f"attachment; filename={filename}")
        email.attach(adjunto_grafico)

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(remitente, password)
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
        return jsonify({"message": "Correo enviado exitosamente"}), 200  # Respuesta exitosa
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return jsonify({"message": "Error al enviar correo"}), 500  # Respuesta de erroooooooor



@app.route('/save-pdf', methods=['POST'])
def save_pdf():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    save_path = os.path.join(app.root_path, file.filename)  # Cambia 'static/pdfs' por tu ruta deseada

    # Asegúrate de que la carpeta exista
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    file.save(save_path)  # Guarda el archivo en el servidor
    return jsonify({"message": "Archivo guardado exitosamente"}), 200

@app.route('/check-file', methods=['GET'])
def check_file():
    filename = "graficoIonic.pdf"
    if os.path.isfile(filename):
        return jsonify({"exists": True}), 200
    else:
        return jsonify({"exists": False}), 404

@app.route('/consultaCategoriasIonic', methods=['GET'])
def consultaCategoriasIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT c.idcategoria, c.nombre, c.tipo, c.descripcion, c.fecha, c.creador, c.activo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM categorias AS c INNER JOIN usuarios AS u ON c.creador = u.documento;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/eliminarCategoriaIonic', methods=['POST'])
def eliminarCategoriaIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("UPDATE categorias SET activo = CASE WHEN activo = 1 THEN 0 ELSE 1 END WHERE idCategoria = %s", ([data['idcategoria']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/agregaCategoriaIonic', methods=['POST'])
def agregaCategoriaIonic():
    try:
        data = request.get_json()

        print(f"Nombre: {data['nombre']}, Tipo: {data['categoria']}, Descripción: {data['descripcion']}, Creador: {data['creador']}")

        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO categorias (nombre, tipo, descripcion, fecha, creador, activo) VALUES (%s, %s, %s, '{fecha}', %s,'1')", (data['nombre'], data['categoria'], data['descripcion'], data['creador']))
        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})
    






# // cosas de edinson urbano no tocar por favor
# // cosas de edinson urbano no tocar por favor
    
    
    #FRANCO
@app.route('/consultaConsumibleIonic', methods=['GET'])
def consultaConsumibleIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre as nombreC FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Insumo' AND consumibles.activo = '1';"
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['foto'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['foto'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['foto'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)
            
        

        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/agregarInsumoIonic', methods=['POST'])
def agregarInsumoIonic():
    try:
        data = request.get_json()

        # Decodificar la imagen de Base64 y guardarla
        if data.get('foto'):
            foto_data = data['foto']

            ahora = datetime.now()
            referencia = "I"+ahora.strftime("%Y%m%d%H%M%S")

            foto_nombre = f"{referencia}.png"  # Puedes cambiar la extensión si es necesario
            foto_path = os.path.join('uploads', foto_nombre)

            # Asegúrate de que la carpeta de destino exista
            os.makedirs('uploads', exist_ok=True)

            # Decodificar y guardar la imagen
            with open(foto_path, "wb") as fh:
                fh.write(base64.b64decode(foto_data.split(',')[1]))

        # Conexión a la base de datos
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')

        cantidad = data.get('cantidad', '0')

        
        tipo = 'Insumo'  

        cursor.execute(
            "INSERT INTO consumibles (idcategoria, nombre, cantidad, foto, tipo, activo, fecha, creador) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (data['idcategoria'], data['nombre'], cantidad, foto_nombre, tipo, '1', fecha, data['creador'])
        )

        connection.commit()
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/eliminarInsumoIonic', methods=['POST'])
def eliminarInsumoIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("UPDATE consumibles SET activo=0 WHERE idObjeto = %s", ([data['idobjeto']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/consultaLiquido1Ionic', methods=['GET'])
def consultaLiquido1Ionic():
    try:
        connection = conexion
        cursor = connection.cursor()
        query = """
        SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, 
            categorias.tipo, categorias.descripcion, categorias.nombre as nombreC 
        FROM consumibles 
        INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria 
        WHERE consumibles.tipo = 'Líquido' AND consumibles.activo = '1';
        """
        cursor.execute(query)
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()

        resultado = []
        for dato in datos:
            registro = dict(zip(column_names, dato))
            # Convertir la imagen a Base64 si existe
            ruta_imagen = os.path.join("uploads", registro['foto'])
            if os.path.exists(ruta_imagen):
                with open(ruta_imagen, "rb") as image_file:
                    registro['foto'] = base64.b64encode(image_file.read()).decode('utf-8')
            else:
                registro['foto'] = None  # Manejar el caso en que la imagen no exista
            resultado.append(registro)

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/agregarLiquidoIonic', methods=['POST'])
def agregarLiquidoIonic():
    try:
        data = request.get_json()

        # Decodificar la imagen de Base64 y guardarla
        if data.get('foto'):
            foto_data = data['foto']

            ahora = datetime.now()
            referencia = "L"+ahora.strftime("%Y%m%d%H%M%S")

            foto_nombre = f"{referencia}.png"
            foto_path = os.path.join('uploads', foto_nombre)

            # Asegúrate de que la carpeta de destino exista
            os.makedirs('uploads', exist_ok=True)

            # Decodificar y guardar la imagen
            with open(foto_path, "wb") as fh:
                fh.write(base64.b64decode(foto_data.split(',')[1]))

        # Conexión a la base de datos
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')

        cantidad = data.get('cantidad', '0') 

        
        tipo = 'Líquido'  

        cursor.execute(
            "INSERT INTO consumibles (idcategoria, nombre, cantidad, foto, tipo, activo, fecha, creador) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (data['idcategoria'], data['nombre'], cantidad, foto_nombre, tipo, '1', fecha, data['creador'])
        )
        connection.commit()
        cursor.close()
        
        return jsonify({"msg": 'ok'})
    except Exception as e:
        return jsonify({"error": str(e)})



@app.route('/eliminarLiquidoIonic', methods=['POST'])
def eliminarLiquidoIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("UPDATE consumibles SET activo=0 WHERE idObjeto = %s", ([data['idobjeto']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/categoriasInsumoIonic', methods=['GET'])
def categoriasInsumoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias WHERE tipo='Insumo' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/categoriasLiquidoIonic', methods=['GET'])
def categoriasLiquidoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias WHERE tipo='Liquido' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/categoriasherraIonic', methods=['GET'])
def categoriasherraIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM categorias WHERE tipo='Herramieta' AND activo='1'")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
    



@app.route('/consultaTodoPrestamosIonic', methods=['GET'])
def consultaTodoPrestamosIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route('/consultaSolicitadosIonic', methods=['GET'])
def consultaSolicitadosIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'S' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'S' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'S' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaPorEntregarIonic', methods=['GET'])
def consultaPorEntregarIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'A' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'A' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'A' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaPrestadoIonic', methods=['GET'])
def consultaPrestadoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'P' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'P' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'P' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaDevueltoIonic', methods=['GET'])
def consultaDevueltoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'D' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'D' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'D' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/consultaRechazadoIonic', methods=['GET'])
def consultaRechazadoIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'R' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'R' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido, fechasoli FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'R' ORDER BY fechasoli DESC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/aceptarPrestamoIonic', methods=['POST'])
def aceptarPrestamoIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"UPDATE servicios SET estado='A' WHERE idservicio = %s", ([data['idservicio']]))

        # cursor.execute(f"UPDATE servicios SET estado = CASE WHEN estado = 'S' THEN 'A' THEN 'S' ELSE 'A' END WHERE idservicio= %s", ([activ['idservicio']]))                       


        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/entregarPrestamoIonic', methods=['POST'])
def entregarPrestamoIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"UPDATE servicios SET estado='P' WHERE idservicio = %s", ([data['idservicio']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/devolverPrestamoIonic', methods=['POST'])
def devolverPrestamoIonic():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"UPDATE servicios SET estado='D' WHERE idservicio = %s", ([data['idservicio']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/rechazarPrestamoIonic', methods=['POST'])
def rechazarPrestamo():
    try:
        data = request.get_json()
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"UPDATE servicios SET estado='R' WHERE idservicio = %s", ([data['idservicio']]))
        connection.commit()
        cursor.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)})
    



