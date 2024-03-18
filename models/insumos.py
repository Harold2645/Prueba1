from conexion import *

class Insumos:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarinsumos(self):
        sql = "SELECT * FROM objetos WHERE tipo='insumos' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosinsumos(self):
        sql = "SELECT * FROM objetos WHERE tipo='insumos'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, insumos):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, cantidad, tipo, activo) VALUES ('{insumos[0]}', '{insumos[1]}', '{insumos[2]}', '{insumos[3]}', 'insumos', '1')"
        self.cursor.execute(sql)        
        self.mysql.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, insumos):
        sql = f"UPDATE objetos SET nombre='{insumos[1]}', idCategoria='{insumos[2]}', cantidad='{insumos[3]}', activo='{insumos[4]}' WHERE idObjeto='{insumos[0]}'"
        self.cursor.execute(sql)        
        self.mysql.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)        
        self.mysql.commit()

misInsumos = Insumos(mysql)
