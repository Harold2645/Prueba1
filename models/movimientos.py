from datetime import datetime
from conexion import *

class Movimientos:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def agregar(self, movimient):
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f"INSERT INTO movimiento (documento,movimiento,fecha,idobjeto) VALUES ('{movimient[0]}','{movimient[1]}','{fecha}','{movimient[2]}')"
        self.cursor.execute(sql)
        self.conexion.commit()

misMovimientos = Movimientos(conexion)

