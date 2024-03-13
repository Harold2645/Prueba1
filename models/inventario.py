from conexion import *

class Tractores:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarTractor(self):
        sql = "SELECT * FROM objetos WHERE tipo='tractor' AND activo='1'"
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
        self.cursor.execute(sql)
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def modificar(self, tractor):
        sql = f"UPDATE objetos SET nombre='{tractor[1]}', idCategoria='{tractor[2]}', estado='{tractor[3]}', disponibilidad='{tractor[4]}', activo='{tractor[5]}' WHERE idObjeto='{tractor[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.conexion.commit()

class Herramientas:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarHerramientas(self):
        sql = "SELECT * FROM objetos WHERE tipo='herramienta' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def todaslasHerramientas(self):
        sql = "SELECT * FROM objetos WHERE tipo='herramienta'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, herramienta):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, estado, disponibilidad, tipo, activo) VALUES ('{herramienta[0]}', '{herramienta[1]}', '{herramienta[2]}', '{herramienta[3]}', '{herramienta[4]}', 'herramienta', '1')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

    def modificar(self, herramienta):
        sql = f"UPDATE objetos SET nombre='{herramienta[1]}', idCategoria='{herramienta[2]}', estado='{herramienta[3]}', disponibilidad='{herramienta[4]}', activo='{herramienta[5]}' WHERE idObjeto='{herramienta[0]}'"
        
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.conexion.commit()

class Insumos:
    def __init__(self, mysql):
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarinsumos(self):
        sql = "SELECT * FROM objetos WHERE tipo='insumos' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def todoslosinsumos(self):
        sql = "SELECT * FROM objetos WHERE tipo='insumos'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, insumos):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, cantidad, tipo, activo) VALUES ('{insumos[0]}', '{insumos[1]}', '{insumos[2]}', '{insumos[3]}', 'insumos', '1')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

    def modificar(self, insumos):
        sql = f"UPDATE objetos SET nombre='{insumos[1]}', idCategoria='{insumos[2]}', cantidad='{insumos[3]}', activo='{insumos[4]}' WHERE idObjeto='{insumos[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.conexion.commit()

class Liquidos:

    def __init__(self, mysql):
        self.mysql = mysql
        self.mysql = mysql
        self.cursor = self.mysql.cursor()
        
    def consultarliquidos(self):
        sql = "SELECT * FROM objetos WHERE tipo='liquidos' AND activo='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def todoslosliquidos(self):
        sql = "SELECT * FROM objetos WHERE tipo='liquidos'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, liquidos):
        sql = f"INSERT INTO objetos (idObjeto, nombre, idCategoria, cantidad, tipo, activo) VALUES ('{liquidos[0]}', '{liquidos[1]}', '{liquidos[2]}', '{liquidos[3]}', 'liquidos', '1')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,idObjeto):
        sql = f"SELECT idObjeto FROM objetos WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado

    def modificar(self, liquidos):
        sql = f"UPDATE objetos SET nombre='{liquidos[1]}', idCategoria='{liquidos[2]}', cantidad='{liquidos[3]}', activo='{liquidos[4]}' WHERE idObjeto='{liquidos[0]}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def borrar(self, idObjeto):
        sql = f"UPDATE objetos SET activo=0 WHERE idObjeto={idObjeto}"
        self.cursor.execute(sql)
        self.conexion.commit()
    
misTracores = Tractores(mysql)
misHerramientas = Herramientas(mysql)
misInsumos = Insumos(mysql)
misLiquidos = Liquidos(mysql)   

