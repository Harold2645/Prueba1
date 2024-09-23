from conexion import *

class Tractores:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    
    def todoslosTractores(self):
        sql = "SELECT tractores.marca, tractores.modelo, tractores.idobjeto, tractores.idcategoria, tractores.fototrac, tractores.activo, categorias.idcategoria, categorias.nombre, categorias.tipo FROM tractores INNER JOIN categorias WHERE tractores.idcategoria = categorias.idcategoria AND categorias.tipo = 'Tractor';"        
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, tractor):
        sql = f"INSERT INTO tractores (idobjeto, idcategoria, fototrac, activo, fechacreacion, creador, marca, modelo,fechamodelo) VALUES ('{tractor[0]}','{tractor[1]}','{tractor[2]}','1','{tractor[3]}','{tractor[4]}','{tractor[5]}','{tractor[6]}','{tractor[7]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

        
    def buscar(self,idObjeto):
        sql = f"SELECT tractores.marca, tractores.modelo,tractores.fechamodelo ,tractores.idobjeto, tractores.idcategoria, tractores.fototrac, tractores.activo, categorias.idcategoria, categorias.nombre, categorias.tipo FROM tractores INNER JOIN categorias WHERE tractores.idcategoria = categorias.idcategoria AND categorias.tipo = 'Tractor' AND idobjeto = '{idObjeto}';"        
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, tractor):
        sql = f"UPDATE tractores SET idCategoria='{tractor[1]}', fototrac='{tractor[2]}',  marca='{tractor[3]}', modelo='{tractor[4]}', fechamodelo='{tractor[5]}', activo='{tractor[6]}' WHERE idObjeto='{tractor[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE tractores SET activo=0 WHERE idObjeto = '{idObjeto}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def mostarTractores(self):
        sql = "SELECT tractores.marca, tractores.modelo, tractores.idobjeto, tractores.idcategoria, tractores.fototrac, tractores.activo, categorias.idcategoria, categorias.nombre, categorias.tipo FROM tractores INNER JOIN categorias WHERE tractores.idcategoria = categorias.idcategoria AND tractores.activo = '1' AND categorias.tipo = 'Tractor';"        
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misTracores = Tractores(conexion)
