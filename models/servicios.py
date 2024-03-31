from conexion import *

class Servicios:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' "
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPedidos(self):
        sql = "SELECT t.marca, t.modelo, s.idobjeto, s.labor, s.documento, s.ficha, s.fechasalida, s.estado, s.idservicio FROM tractores AS t INNER JOIN servicios AS s ON t.idobjeto = s.idobjeto WHERE t.activo = '1' AND s.tipo = 'Tractor' AND s.estado = '1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPrestado(self):
        sql = "SELECT * FROM servicios WHERE estado='2'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevuelto(self):
        sql = "SELECT * FROM servicios WHERE estado='3'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPorEntregar(self):
        sql = "SELECT * FROM servicios WHERE estado='4'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarCancelado(self):
        sql = "SELECT * FROM servicios WHERE estado='0'"
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
        sql = f"INSERT INTO servicios (idobjeto, labor, documento, ficha, fechasalida, cantidad, tipo, estado) VALUES ('{pedir[0]}','{pedir[1]}','{pedir[2]}','{pedir[3]}','{pedir[4]}','{pedir[5]}','{pedir[6]}','1')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def aceptarPrestamo(self, id):
        sql = f"UPDATE servicios  SET estado='4' WHERE idservicio={id}"
        self.cursor.execute(sql)
        self.conexion.commit()



misServicios = Servicios(conexion)