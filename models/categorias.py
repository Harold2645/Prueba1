from conexion import *

class Categorias:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
        
    def consultarCategorias(self):
        sql = "SELECT c.idcategoria, c.nombre, c.tipo, c.descripcion, c.fecha, c.creador, c.activo, u.nombre AS usuario_nombre, u.apellido AS usuario_apellido FROM categorias AS c INNER JOIN usuarios AS u ON c.creador = u.documento;"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def categoriasTractor(self):
        sql = "SELECT * FROM categorias WHERE tipo='Tractor' AND activo='1' "
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasHerramienta(self):
        sql = "SELECT * FROM categorias WHERE tipo='Herramienta' AND activo='1'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasInsumos(self):
        sql = "SELECT * FROM categorias WHERE tipo='Insumo' AND activo='1'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias

    def categoriasLiquidos(self):
        sql = "SELECT * FROM categorias WHERE tipo='Liquido' AND activo='1'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias


    def agregarCategoria(self, categ):
        sql = f"INSERT INTO `categorias` (`nombre`, `tipo`, `descripcion`, `fecha`, `creador`, `activo`) VALUES ('{categ[0]}', '{categ[1]}', '{categ[2]}', '{categ[3]}', '{categ[4]}', '1')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrarCategoria(self, idCategoria):
        sql = f"UPDATE categorias SET activo='0' WHERE idCategoria = '{idCategoria}'"
        self.cursor.execute(sql)
        self.conexion.commit()


    def activarCategoria(self, idCategoria):
        sql = f"UPDATE categorias SET activo='1' WHERE idCategoria = '{idCategoria}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def buscarCate(self):
        sql = "SELECT descripcion FROM categorias"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misCategorias=Categorias(conexion)