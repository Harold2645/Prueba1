from conexion import *

class Servicios:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT * FROM servicios"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPedidos(self):
        sql = "SELECT * FROM servicios WHERE estado='1'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarPrestado(self):
        sql = "SELECT * FROM servicios WHERE estado='2'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarDevuelto(self):
        sql = "SELECT * FROM servicios WHERE estado='3'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def consultarCancelado(self):
        sql = "SELECT * FROM servicios WHERE estado='0'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado





misServicios = Servicios(conexion)