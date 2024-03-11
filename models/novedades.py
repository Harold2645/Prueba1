from conexion import *

class novedades:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()

    def agregarNovedad(self, idobjeto, documento, tipo, fecha, descripcion, foto):
        sql = "INSERT INTO `novedades` ( `idobjeto`, `documento`, `tipo`, `fecha`, `descripcion`, `foto`) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (idobjeto, documento, tipo, fecha, descripcion, foto))
        self.mysql.commit()
        
    def consultarNovedades(self):
        sql = "SELECT * FROM novedades"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
misNovedades=novedades(mysql)