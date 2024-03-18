from conexion import *

class Insumos:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarinsumos(self):
        sql = "SELECT * FROM consumibles WHERE tipo='Insumo' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosinsumos(self):
        sql = "SELECT * FROM consumibles WHERE tipo='Insumo'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, insumos):
        sql = f"INSERT INTO `consumibles` (`idcategoria`, `nombre`, `cantidad`, `tipo`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{insumos[0]}', '{insumos[1]}', '{insumos[2]}', 'Insumo', '{insumos[3]}', '1', '{insumos[4]}', '{insumos[5]}')"
        self.cursor.execute(sql)        
        self.mysql.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT * FROM consumibles WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, insumos):
        sql = f"UPDATE consumibles SET nombre='{insumos[1]}', idCategoria='{insumos[2]}', cantidad='{insumos[3]}', activo='{insumos[4]}', foto='{insumos[5]}' WHERE idconsumible='{insumos[0]}'"
        self.cursor.execute(sql)        
        self.mysql.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE consumibles SET activo=0 WHERE idconsumible={idObjeto}"
        self.cursor.execute(sql)        
        self.mysql.commit()

misInsumos = Insumos(mysql)
