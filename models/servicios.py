from conexion import *

    #Solicitado     =   S
    #Aceptado       =   A
    #Por entregar   =   E
    #Prestado       =   P
    #Devuelto       =   D
    #Rechazado      =   R


class Servicios:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarSolicitados(self):
        sql = "SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'S' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'S' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'S' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarAceptado(self):
        sql = "SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'A' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'A' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'A' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado


    def consultarPrestado(self):
        sql = "SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'P' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'P' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'P' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevuelto(self):
        sql = "SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'D' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'D' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'D' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarRechazado(self):
        sql = "SELECT t.marca AS nombre, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'R' UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'R' UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'R' ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscarTractor(self, idObjeto):
        sql = f"SELECT idobjeto, marca FROM tractores WHERE idObjeto='{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscarHerramienta(self, idObjeto):
        sql = f"SELECT idobjeto, nombre FROM herramientas WHERE idObjeto='{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def buscarInsumo(self, idObjeto):
        sql = f"SELECT idobjeto, nombre FROM consumibles WHERE idobjeto='{idObjeto}' AND tipo='Insumo'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscarLiquido(self, idObjeto):
        sql = f"SELECT idobjeto, nombre FROM consumibles WHERE idobjeto='{idObjeto}' AND tipo='Liquido'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def pedir(self, pedir):
        sql = f"INSERT INTO servicios (idobjeto, labor, documento, ficha, fechasalida, cantidad, tipo, estado) VALUES ('{pedir[0]}','{pedir[1]}','{pedir[2]}','{pedir[3]}','{pedir[4]}','{pedir[5]}','{pedir[6]}','S')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def aceptarPrestamo(self, id):
        sql = f"UPDATE servicios  SET estado='A' WHERE idservicio='{id}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def prestado(self, servi):
        sql = f"UPDATE servicios  SET estadosalida='{servi[1]}', encargado='{servi[2]}', estado='P' WHERE idservicio='{servi[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
    
    def devuelto(self, devo):
        sql = f"UPDATE servicios  SET fechaentrada='{devo[1]}', descripcion='{devo[2]}', foto='{devo[3]}', estado='D' WHERE idservicio='{devo[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def rechazarPrestamo(self, id):
        sql = f"UPDATE servicios  SET estado='R' WHERE idservicio='{id}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def consultarMios(self, id):
        sql = f"SELECT * FROM (SELECT t.marca AS nombre, t.modelo AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Tractor' AS tipo FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.documento = {id} UNION ALL SELECT h.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Herramienta' AS tipo FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.documento = {id} UNION ALL SELECT c.nombre, NULL AS modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio, 'Insumo' AS tipo FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.documento = {id}) AS combined_results ORDER BY fechasalida DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar(self,id):
        sql = f"SELECT * FROM (SELECT t.marca AS objeto_nombre, s.idobjeto, s.documento, s.fechaentrada AS fecha, s.descripcion, s.foto, s.tipo AS tipo, s.idservicio AS idservicio, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE s.idservicio = {id} UNION ALL SELECT h.nombre AS objeto_nombre, s.idobjeto, s.documento, s.fechaentrada AS fecha, s.descripcion, s.foto, s.tipo AS tipo, s.idservicio AS idservicio, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE s.idservicio = {id} UNION ALL SELECT c.nombre AS objeto_nombre, s.idobjeto, s.documento, s.fechaentrada AS fecha, s.descripcion, s.foto, s.tipo AS tipo, s.idservicio AS idservicio, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto INNER JOIN usuarios AS u ON s.documento = u.documento WHERE s.idservicio = {id}) AS combined_results ORDER BY fecha DESC;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    #Solicitado     =   S
    #Aceptado       =   A
    #Prestado       =   P
    #Devuelto       =   D
    #Rechazado      =   R

misServicios = Servicios(conexion)