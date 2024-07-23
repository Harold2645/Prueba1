from conexion import *

class novedades:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def agregarNovedad(self, novedad):
        sql = f"INSERT INTO novedades (idobjeto, documento, tipo, fecha, descripcion, foto) VALUES ('{novedad[0]}', '{novedad[1]}', '{novedad[2]}', '{novedad[3]}', '{novedad[4]}', '{novedad[5]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def consultarNovedades(self):
        sql = "SELECT * FROM (SELECT t.marca AS nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM tractores AS t INNER JOIN novedades AS n ON t.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento UNION ALL SELECT h.nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM herramientas AS h INNER JOIN novedades AS n ON h.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento UNION ALL SELECT c.nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM consumibles AS c INNER JOIN novedades AS n ON c.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento) AS combined_results ORDER BY fecha DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar(self,id):
        sql = f"SELECT * FROM (SELECT t.marca AS objeto_nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM tractores AS t INNER JOIN novedades AS n ON t.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento WHERE n.idnovedad = {id} UNION ALL SELECT h.nombre AS objeto_nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM herramientas AS h INNER JOIN novedades AS n ON h.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento WHERE n.idnovedad = {id} UNION ALL SELECT c.nombre AS objeto_nombre, n.idobjeto, n.documento, n.fecha, n.descripcion, n.foto, n.tipo AS tipo, n.idnovedad, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM consumibles AS c INNER JOIN novedades AS n ON c.idobjeto = n.idobjeto INNER JOIN usuarios AS u ON n.documento = u.documento WHERE n.idnovedad = {id}) AS combined_results ORDER BY fecha DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misNovedades=novedades(conexion)