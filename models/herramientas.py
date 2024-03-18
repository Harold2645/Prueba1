from conexion import *

class Herramientas:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarHerramientas(self):
        sql = "SELECT * FROM objetos WHERE tipo='herramienta' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todaslasHerramientas(self):
        sql = "SELECT * FROM objetos WHERE tipo='herramienta'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, herramienta):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, estado, disponibilidad, tipo, activo) VALUES ('{herramienta[0]}', '{herramienta[1]}', '{herramienta[2]}', '{herramienta[3]}', '{herramienta[4]}', 'herramienta', '1')"
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, herramienta):
        sql = f"UPDATE objetos SET nombre='{herramienta[1]}', idCategoria='{herramienta[2]}', estado='{herramienta[3]}', disponibilidad='{herramienta[4]}', activo='{herramienta[5]}' WHERE idObjeto='{herramienta[0]}'"
        self.cursor.execute(sql)
        self.mysql.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.mysql.commit()

misHerramientas = Herramientas(mysql)
