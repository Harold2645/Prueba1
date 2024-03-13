from conexion import *

class Categorias:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarCategorias(self):
        sql = "SELECT * FROM categoria"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def categoriasTractor(self):
        sql = "SELECT * FROM categoria WHERE tipo='Tractor'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasHerramienta(self):
        sql = "SELECT * FROM categoria WHERE tipo='Herramienta'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias
    
    def categoriasConsumibles(self):
        sql = "SELECT * FROM categoria WHERE tipo='Consumible'"
        self.cursor.execute(sql)
        categorias = self.cursor.fetchall()
        return categorias

    def agregarCategoria(self, categ):
        sql = f"INSERT INTO categoria (nombre, tipo) VALUES ('{categ[0]}', '{categ[1]}')"
        self.cursor.execute(sql)
        
    def borrarCategoria(self, idCategoria):
        sql = f"DELETE FROM categoria WHERE `idCategoria` = {idCategoria}"
        self.cursor.execute(sql)




misCategorias=Categorias(mysql)