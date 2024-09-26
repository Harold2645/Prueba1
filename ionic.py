import base64
from conexion import *
import hashlib
from datetime import datetime
from flask import jsonify, request


@app.route('/loginIonic', methods=['POST'])
def loginIonic():
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
        print(e)
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
            foto_nombre = f"{data['idobjeto']}.png"  # Puedes cambiar la extensión si es necesario
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
        print(data)
        connection = conexion
        cursor = connection.cursor()
        fecha = datetime.now().strftime("%Y%m%d%H%M%S")
        cursor.execute(f"INSERT INTO servicios (idobjeto, labor, documento, ficha, fechasalida, cantidad, tipo, estado,fechasoli) VALUES (%s, %s, %s, %s,%s, %s, %s,'S','{fecha}')", (data['idobjeto'],data['labor'],data['documento'],data['ficha'],data['fechasalida'],data['cantidad'],data['tipo']))
        connection.commit()
        print("Funciono")
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        print(e)
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
        print("funciono")
        cursor.close()
        return jsonify({"msg": 'ok'})
    except Exception as e:
        print(e)
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
        print(e)
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
        print(datos)
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
        print(e)

@app.route('/datosgrafLiquidosIonic', methods=['GET'])
def datosgrafLiquidosIonic():
    try:
        connection = conexion
        cursor = connection.cursor()
        cursor.execute(f"SELECT nombre, cantidad FROM consumibles WHERE tipo = 'Liquido' GROUP BY nombre ORDER BY nombre ASC;")
        column_names = [column[0] for column in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        return jsonify([dict(zip(column_names, dato)) for dato in datos])
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
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
        print(e)
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
        print(e)
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
    
    
    
