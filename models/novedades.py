from conexion import *

class novedades:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()

    def agregarNovedad(self, novedad):
        sql = f"INSERT INTO novedades (`idobjeto`, `documento`, `tipo`, `fecha`, `descripcion`, `foto`, `creador`) VALUES ('{novedad[0]}', '{novedad[1]}', '{novedad[2]}', '{novedad[3]}', '{novedad[4]}', '{novedad[5]}', '{novedad[6]}')"
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def consultarNovedades(self):
        sql = "SELECT * FROM novedades"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar(self,idObjeto):
        sql = f"SELECT * FROM novedades WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misNovedades=novedades(mysql)