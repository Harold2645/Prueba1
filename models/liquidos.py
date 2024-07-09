from conexion import *

class Liquidos:

    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
        
    def consultarliquidos(self):
        sql = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Liquido' AND consumibles.activo = '1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todoslosliquidos(self):
        sql = "SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.nombre, consumibles.activo FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Liquido';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, liquidos):
        sql = f"INSERT INTO `consumibles` (`idcategoria`, `nombre`, `cantidad`, `tipo`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{liquidos[0]}', '{liquidos[1]}', '{liquidos[2]}', 'Liquido', '{liquidos[3]}', '1', '{liquidos[4]}', '{liquidos[5]}')"
        self.cursor.execute(sql)        
        self.conexion.commit()

        
    def buscar(self,idObjeto):
        sql = f"SELECT consumibles.idobjeto, consumibles.nombre, consumibles.cantidad, consumibles.foto, categorias.tipo, categorias.descripcion, categorias.idcategoria, categorias.nombre, consumibles.activo FROM consumibles INNER JOIN categorias ON categorias.idcategoria = consumibles.idcategoria WHERE consumibles.tipo = 'Liquido' AND idObjeto='{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, liquidos):
        sql = f"UPDATE consumibles SET nombre='{liquidos[1]}', idCategoria='{liquidos[2]}', cantidad='{liquidos[3]}', foto='{liquidos[4]}', activo='{liquidos[5]}' WHERE idobjeto='{liquidos[0]}'"
        self.cursor.execute(sql)        
        self.conexion.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE consumibles SET activo='0' WHERE idobjeto='{idObjeto}'"
        self.cursor.execute(sql)        
        self.conexion.commit()

    def buscarnombre(self,idObjeto):
        sql = f"SELECT nombre FROM consumibles WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misLiquidos = Liquidos(conexion)   
