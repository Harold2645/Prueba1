from conexion import *

class Tractores:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarTractor(self):
        sql = "SELECT * FROM objetos WHERE tipo='tractor'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosTractores(self):
        sql = "SELECT * FROM objetos WHERE tipo='tractor'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, tractor):
        sql = f"INSERT INTO `objetos` (`idobjeto`, `idcategoria`, `nombre`, `disponibilidad`, `tipo`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{tractor[0]}', '{tractor[1]}', '{tractor[2]}', '{tractor[3]}', 'tractor', '{tractor[4]}', '1', '{tractor[5]}', '{tractor[6]}')"
        print(sql)
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, tractor):
        sql = f"UPDATE objetos SET nombre='{tractor[1]}', idCategoria='{tractor[2]}', estado='{tractor[3]}', disponibilidad='{tractor[4]}', activo='{tractor[5]}' WHERE idObjeto='{tractor[0]}'"
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.mysql.commit()

misTracores = Tractores(mysql)
