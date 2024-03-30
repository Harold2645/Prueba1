from conexion import *

class Herramientas:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
        
    def consultarHerramientas(self):
        sql = "SELECT herramientas.idobjeto, herramientas.nombre, herramientas.foto, categorias.tipo, categorias.descripcion FROM herramientas INNER JOIN categorias ON categorias.idcategoria = herramientas.idcategoria WHERE herramientas.activo='1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def todaslasHerramientas(self):
        sql = "SELECT herramientas.idobjeto, herramientas.nombre, herramientas.foto, categorias.tipo, categorias.descripcion FROM herramientas INNER JOIN categorias ON categorias.idcategoria = herramientas.idcategoria;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, herramienta):
        sql = f"INSERT INTO `herramientas` (`idobjeto`, `idcategoria`, `nombre`, `cantidad`, `foto`, `activo`, `fecha`, `creador`) VALUES ('{herramienta[0]}', '{herramienta[1]}', '{herramienta[2]}', '{herramienta[3]}', '{herramienta[4]}', '1', '{herramienta[5]}', '{herramienta[6]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT herramientas.idobjeto, herramientas.nombre, herramientas.foto, categorias.tipo, categorias.descripcion, categorias.idcategoria, categorias.nombre FROM herramientas INNER JOIN categorias ON categorias.idcategoria = herramientas.idcategoria WHERE herramientas.activo='1' AND idobjeto = '{idObjeto}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, herramienta):
        sql = f"UPDATE herramientas SET nombre='{herramienta[1]}', idCategoria='{herramienta[2]}', foto='{herramienta[3]}' WHERE idobjeto='{herramienta[0]}'"

        self.cursor.execute(sql)
        self.conexion.commit()

        
    def borrar(self, idObjeto):
        sql = f"UPDATE herramientas SET activo=0 WHERE idobjeto='{idObjeto}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def buscarPornombre(self, nombre):
        sql = f"SELECT herramientas.idobjeto, herramientas.nombre, herramientas.foto, categorias.tipo, categorias.descripcion FROM herramientas INNER JOIN categorias ON categorias.nombre = herramientas.nombre WHERE herramientas.nombre LIKE '%{nombre}%' AND activo='1';"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misHerramientas = Herramientas(conexion)
