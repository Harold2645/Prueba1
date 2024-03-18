from conexion import *

class Liquidos:

    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarliquidos(self):
        sql = "SELECT * FROM objetos WHERE tipo='liquidos' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosliquidos(self):
        sql = "SELECT * FROM objetos WHERE tipo='liquidos'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, liquidos):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, cantidad, tipo, activo) VALUES ('{liquidos[0]}', '{liquidos[1]}', '{liquidos[2]}', '{liquidos[3]}', 'liquidos', '1')"
        self.cursor.execute(sql)        
        self.mysql.commit()

        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, liquidos):
        sql = f"UPDATE objetos SET nombre='{liquidos[1]}', idCategoria='{liquidos[2]}', cantidad='{liquidos[3]}', activo='{liquidos[4]}' WHERE idObjeto='{liquidos[0]}'"
        self.cursor.execute(sql)        
        self.mysql.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)        
        self.mysql.commit()

misLiquidos = Liquidos(mysql)   
