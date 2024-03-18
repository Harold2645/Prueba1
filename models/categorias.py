from conexion import *

class Categorias:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarCategorias(self):
        sql = "SELECT * FROM categorias"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def categoriasTractor(self):
        sql = "SELECT * FROM categorias WHERE tipo='Tractor'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasHerramienta(self):
        sql = "SELECT * FROM categorias WHERE tipo='Herramienta'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasInsumos(self):
        sql = "SELECT * FROM categorias WHERE tipo='Insumos'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias

    def categoriasLiquidos(self):
        sql = "SELECT * FROM categorias WHERE tipo='Liquidos'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias


    def agregarCategoria(self, categ):
        sql = f"INSERT INTO `categorias` (`nombre`, `tipo`, `descripcion`, `fecha`, `creador`) VALUES ('{categ[0]}', '{categ[1]}', '{categ[2]}', '{categ[3]}', '{categ[4]}')"
        self.cursor.execute(sql)
        self.mysql.commit()
        
    def borrarCategoria(self, idCategoria):
        sql = f"DELETE FROM categorias WHERE `idCategoria` = {idCategoria}"
        self.cursor.execute(sql)

    def buscarCate(self):
        sql = "SELECT descripcion FROM categorias"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misCategorias=Categorias(mysql)