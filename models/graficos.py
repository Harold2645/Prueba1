from conexion import *

class Graficos:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()
    
    def datosTractores(self):
        sql = "SELECT servicios.cantidad, servicios.fechasalida, tractores.marca FROM servicios INNER JOIN tractores ON tractores.idobjeto = servicios.idobjeto WHERE servicios.tipo = 'Tractor' AND tractores.activo = '1'"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
    
    def datosConsumibles(self):
        sql = "SELECT nombre, cantidad FROM consumibles WHERE tipo = 'Liquido' GROUP BY nombre ORDER BY nombre ASC;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
      
misGraficos=Graficos(conexion)






