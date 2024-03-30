from conexion import *

class Insumos:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
        
    def consultarinsumos(self):
        sql = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Insumo' AND consumibles.activo = '1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosinsumos(self):
        sql = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Insumo';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, insumos):
        sql = f"INSERT INTO `consumibles` (`idcategoria`, `nombre`, `cantidad`, `tipo`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{insumos[0]}', '{insumos[1]}', '{insumos[2]}', 'Insumo', '{insumos[3]}', '1', '{insumos[4]}', '{insumos[5]}')"
        self.cursor.execute(sql)        
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.idcategoria, categorias.nombre FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Insumo' AND idObjeto='{idObjeto}';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, insumos):
        sql = f"UPDATE consumibles SET nombre='{insumos[1]}', idcategoria='{insumos[2]}', cantidad='{insumos[3]}', foto='{insumos[4]}' WHERE idobjeto='{insumos[0]}'"
        self.cursor.execute(sql)        
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE consumibles SET activo=0 WHERE idobjeto='{idObjeto}'"
        self.cursor.execute(sql)        
        self.conexion.commit()


    def buscarPornombre(self, nombre):
        sql = f"SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.nombre LIKE '%{nombre}%' AND consumibles.tipo = 'Insumo' AND consumibles.activo = '1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def buscarnombre(self,idObjeto):
        sql = f"SELECT nombre FROM consumibles WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misInsumos = Insumos(conexion)
