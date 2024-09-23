from conexion import conexion
from datetime import datetime
from models.tractores import Tractores
import pytest

ahora = datetime.now()

@pytest.fixture(scope="class")
def setup_and_teardown():
    # Configuración de la conexión y Tractores
    conexion_db = conexion
    misTractores = Tractores(conexion_db)
    yield misTractores
    # Limpieza después de todas las pruebas
    sql = "DELETE FROM tractores WHERE idobjeto IN ('ABC123123', 'DEF456456', 'GHI789789')"
    misTractores.cursor.execute(sql)
    conexion_db.commit()

@pytest.mark.parametrize(
    "tractor",
    [
        ("ABC123123", "Tractor", "foto1", ahora, "1234567890", "ferguson", "52024", "2014"),
        ("DEF456456", "Tractor", "foto2", ahora, "0987654321", "john_deere", "X750", "2018"),
        ("GHI789789", "Tractor", "foto3", ahora, "1122334455", "kubota", "BX238", "2020")
    ]
)
class TestTractores:

    def test_agregar_tractor(self, setup_and_teardown, tractor):
        misTractores = setup_and_teardown

        # Verificar si el tractor ya existe y eliminarlo si es necesario
        sql = f"DELETE FROM tractores WHERE idobjeto='{tractor[0]}'"
        misTractores.cursor.execute(sql)
        misTractores.conexion.commit()

        # Llamar a la función agregar
        misTractores.agregar(tractor)
        
        # Verificar si el tractor fue agregado correctamente
        sql = f"SELECT idobjeto, modelo FROM tractores WHERE idobjeto='{tractor[0]}'"
        misTractores.cursor.execute(sql)
        resultado = misTractores.cursor.fetchone()
        
        assert resultado is not None, f"El tractor con ID {tractor[0]} no fue encontrado en la base de datos."
        assert resultado[0] == tractor[0], f"ID del objeto esperado: {tractor[0]}, pero se encontró: {resultado[0]}"
        assert resultado[1] == tractor[6], f"Modelo esperado: {tractor[6]}, pero se encontró: {resultado[1]}"