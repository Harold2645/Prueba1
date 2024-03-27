from conexion import *

class Tractores:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
        
    def consultarTractor(self):
        sql = "SELECT * FROM tractores WHERE activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosTractores(self):
        sql = "SELECT * FROM tractores"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, tractor):
        sql = f"INSERT INTO tractores (idobjeto, idcategoria, fototrac, activo, fechacreacion, creador, marca, modelo) VALUES ('{tractor[0]}','{tractor[1]}','{tractor[2]}','1','{tractor[3]}','{tractor[4]}','{tractor[5]}','{tractor[6]}')"
        print(sql)
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT * FROM tractores WHERE idObjeto='{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, tractor):
        sql = f"UPDATE objetos SET nombre='{tractor[1]}', idCategoria='{tractor[2]}', estado='{tractor[3]}', disponibilidad='{tractor[4]}', activo='{tractor[5]}' WHERE idObjeto='{tractor[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE tractores SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.conexion.commit()

misTracores = Tractores(conexion)
