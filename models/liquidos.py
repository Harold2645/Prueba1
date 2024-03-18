from conexion import *

class Liquidos:

    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarliquidos(self):
        sql = "SELECT * FROM consumibles WHERE tipo='liquido' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosliquidos(self):
        sql = "SELECT * FROM consumibles WHERE tipo='liquido'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, liquidos):
        sql = f"INSERT INTO `consumibles` (`idcategoria`, `nombre`, `cantidad`, `tipo`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{liquidos[0]}', '{liquidos[1]}', '{liquidos[2]}', 'Liquido', '{liquidos[3]}', '1', '{liquidos[4]}', '{liquidos[5]}')"
        self.cursor.execute(sql)        
        self.mysql.commit()

        
    def buscar(self,idObjeto):
        sql = f"SELECT * FROM consumibles WHERE idconsumible={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, liquidos):
        sql = f"UPDATE consumibles SET nombre='{liquidos[1]}', idCategoria='{liquidos[2]}', cantidad='{liquidos[3]}', activo='{liquidos[4]}' WHERE idconsumible='{liquidos[0]}'"
        self.cursor.execute(sql)        
        self.mysql.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE consumibles SET activo=0 WHERE idconsumible={idObjeto}"
        self.cursor.execute(sql)        
        self.mysql.commit()

misLiquidos = Liquidos(mysql)   
