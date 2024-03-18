from conexion import *

class Herramientas:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarHerramientas(self):
        sql = "SELECT * FROM herramientas WHERE activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todaslasHerramientas(self):
        sql = "SELECT * FROM herramientas"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, herramienta):
        sql = f"INSERT INTO `herramientas` (`idobjeto`, `idcategoria`, `nombre`, `cantidad`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{herramienta[0]}', '{herramienta[1]}', '{herramienta[2]}', '{herramienta[3]}', '{herramienta[4]}', '1', '{herramienta[5]}', '{herramienta[6]}')"
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT * FROM herramientas WHERE idobjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, herramienta):
        sql = f"UPDATE herramientas SET nombre='{herramienta[1]}', idCategoria='{herramienta[2]}', cantidad='{herramienta[3]}', activo='{herramienta[4]}', foto='{herramienta[5]}' WHERE idobjeto='{herramienta[0]}'"

        self.cursor.execute(sql)
        self.mysql.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE herramientas SET activo=0 WHERE idobjeto={idObjeto}"
        self.cursor.execute(sql)
        self.mysql.commit()

misHerramientas = Herramientas(mysql)
