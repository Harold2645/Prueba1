import pytest
from unittest.mock import patch, MagicMock
from routes.tractores import agregarTrac
from models.tractores import misTracores
from datetime import datetime

@pytest.fixture
def mock_dependencies():
    with patch('models.tractores.misTracores.agregarTrac') as mock_agregar:
        yield mock_agregar

@pytest.mark.parametrize(
    "creador, idobjeto, categoria, foto, hora, fechacreacion, marca, modelo, fechamodelo",
    [
        ("edinson", "ACB123", "tractor", "ahora", datetime(2024, 8, 27, 10, 0, 0), "ferguson", "modelX", "2024-08-01")
    ]
)
def test_agregarTrac(mock_dependencies, creador, idobjeto, categoria, foto, hora, fechacreacion, marca, modelo, fechamodelo):
    # Configurar el mock
    mock_dependencies.return_value = True  # Simular que el agregarTrac se ejecuta correctamente

    # Crear un objeto de datos que simule la entrada
    data = {
        'creador': creador,
        'idobjeto': idobjeto,
        'categoria': categoria,
        'foto': foto,
        'hora': hora,
        'fechacreacion': fechacreacion,
        'marca': marca,
        'modelo': modelo,
        'fechamodelo': fechamodelo
    }

    # Llamar a la función que quieres probar
    resultado = agregarTrac(data)

    # Verificar que el método agregarTrac fue llamado con los parámetros correctos
    mock_dependencies.assert_called_once_with(
        creador=creador,
        idobjeto=idobjeto,
        categoria=categoria,
        foto=foto,
        hora=hora,
        fechacreacion=fechacreacion,
        marca=marca,
        modelo=modelo,
        fechamodelo=fechamodelo
    )

    # Verificar el resultado esperado
    assert resultado == True  # O cualquier resultado que esperes
