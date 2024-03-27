from conexion import *

class Usuario:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def consultar(self):
        sql = "SELECT * FROM usuarios WHERE activo=1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    
    def buscar(self,documento):
        sql = f"SELECT * FROM usuarios WHERE documento={documento}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def agregar(self, usuarios):
        sql = f"INSERT INTO usuarios (documento,nombre,apellido,celular,contrasena,rol,ficha,fecha,activo) VALUES ('{usuarios[0]}','{usuarios[1]}','{usuarios[2]}','{usuarios[3]}','{usuarios[4]}','{usuarios[5]}','{usuarios[6]}','{usuarios[7]}',2)"
        self.cursor.execute(sql)
        self.conexion.commit()
    
    def consultAcepta(self):
        sql = "SELECT * FROM usuarios WHERE activo=2"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def aceptarSi(self, documento):
        sql = f"UPDATE usuarios  SET activo=1 WHERE documento={documento}"
        self.cursor.execute(sql)
        self.conexion.commit()

    def actualizar(self,usuarios,documento):
        sql = f"UPDATE usuarios SET nombre='{usuarios[1]},apelldio='{usuarios[2]},celular='{usuarios[3]},contrasena='{usuarios[4]},rol='{usuarios[5]},ficha='{usuarios[6]} WHERE documento = {documento}"
        self.cursor.execute(sql)
        self.conexion.commit()

    def borrar(self, documento):
        sql = f"UPDATE usuarios SET activo=0 WHERE documento={documento}"
        self.cursor.execute(sql)
        self.conexion.commit()

    def buscarFicha(self):
        sql = "SELECT ficha FROM usuarios"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

misUsuarios=Usuario(conexion)