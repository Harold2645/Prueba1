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

    def consultarTractor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarSolicitadosTractor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'S';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarSolicitadosHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'S';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarSolicitadosConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'S';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarAceptadoTractor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'A';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarAceptadoHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'A';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarAceptadoConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'A';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarPrestadoTracor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'P';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPrestadoHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'P';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPrestadoConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'P';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevueltoTractor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'D';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevueltoHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'D';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevueltoConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'D';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def consultarRechazadoTractor(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = 'R';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarRechazadoHerramienta(self):
        sql = "SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.estado = 'R';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarRechazadoConsumible(self):
        sql = "SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.estado = 'R';"
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
        sql = f"SELECT idobjeto, nombre FROM consumibles WHERE idobjeto='{idObjeto}'"
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
        print(servi)
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

    def consultarTractorMios(self, id):
        sql = f"SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.documento = {id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarHerramientaMios(self, id):
        sql = f"SELECT h.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM herramientas AS h INNER JOIN servicios AS s ON h.idobjeto = s.idobjeto WHERE h.activo = '1' AND s.tipo = 'Herramienta' AND s.documento = {id};"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarConsumibleMios(self, id):
        sql = f"SELECT c.nombre, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM consumibles AS c INNER JOIN servicios AS s ON c.idobjeto = s.idobjeto WHERE c.activo = '1' AND s.tipo = 'Insumo' AND s.documento = {id};"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    #Solicitado     =   S
    #Aceptado       =   A
    #Prestado       =   P
    #Devuelto       =   D
    #Rechazado      =   R

misServicios = Servicios(conexion)