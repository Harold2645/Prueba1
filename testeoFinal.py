from conexion import *
from datetime import datetime
from models.tractores import misTracores
import pytest


ahora = datetime.now()

class Test_tractores:

    ahora = datetime.now()

    @pytest.mark.parametrize(
        ["idobjeto", "idcategoria", "fototrac", "activo", "fechacreacion", "creador", "marca", "modelo","fechamodelo", "esperado"],
        [("ABC123123", "Tractor", "foto", "1", ahora, "1234567890", "ferguson", "52024", "2014", True )]
    )
    
    def setup_method(self):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    # def teardown_method(self):
    #     self.cursor.close()
    #     self.conexion.close()

    def teardown_class(self):
        # Limpiar la base de datos
        sql=f"DELETE FROM tractores WHERE idobjeto='ABC123123'"
        cursor = conexion.cursor()
        cursor.execute(sql)
        conexion.commit()

    def test_agrege_tractor(self):
        idobjetoo= "ABC123123"
        categoria= "Tractor"
        fotot= "foto"
        fechacreacion= ahora
        creador= "1234567890"
        marca= "ferguson"
        modelo= "52024"
        fechamodelo= "2014"

        # print(idobjeto)

        sql = f"INSERT INTO tractores (idobjeto, idcategoria, fototrac, activo, fechacreacion, creador, marca, modelo,fechamodelo) VALUES ('{idobjetoo}','{categoria}','{fotot}','1','{fechacreacion}','{creador}','{marca}','{modelo}','{fechamodelo}')"
        self.cursor.execute(sql)
        self.conexion.commit()

        sql = f"SELECT idobjeto, modelo FROM tractores WHERE idobjeto='{idobjetoo}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        
        idobjetoFnl = resultado[0][0] 

        print(idobjetoo)
        print(idobjetoFnl)

        assert idobjetoFnl == idobjetoo
