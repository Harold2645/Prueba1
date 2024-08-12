from conexion import *

class Envios:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()


    def datoacpm(self):
        sql = "SELECT cantidad, nombre, tipo FROM consumibles WHERE nombre = 'ACPM' AND cantidad <= 25"
        self.cursor.execute(sql) 
        data = self.cursor.fetchall()
        return data
    
misEnvios=Envios(conexion)