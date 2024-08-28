import pytest
from flask import Flask, session
from werkzeug.datastructures import FileStorage
from io import BytesIO
from routes.tractores import *  # Asegúrate de que `app` es la instancia de tu Flask

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_agregarTrac_admin(client):
    # Simula una sesión de usuario autenticado como Admin
    with client.session_transaction() as sess:
        sess['loginCorrecto'] = True
        sess['rol'] = 'Admin'
        sess['documento'] = '123456'

    # Simula una solicitud POST
    data = {
        'idobjeto': '1234',
        'idcategoria': 'Cat1',
        'marca': 'MarcaTest',
        'modelo': 'ModeloTest',
        'fechamodelo': '2024-01-01'
    }
    photo = FileStorage(stream=BytesIO(b'photo_data'), filename='photo.jpg')

    response = client.post(
        '/guardarTractor',
        data=data,
        content_type='multipart/form-data',
        follow_redirects=True,
        buffered=True,
        files={'fototrac': photo}
    )

def test_agregarTrac_no_login(client):
    # Simula una solicitud POST sin sesión autenticada
    data = {
        'idobjeto': '1234',
        'idcategoria': 'Cat1',
        'marca': 'MarcaTest',
        'modelo': 'ModeloTest',
        'fechamodelo': '2024-01-01'
    }
    photo = FileStorage(stream=BytesIO(b'photo_data'), filename='photo.jpg')
    response = client.post('/guardarTractor', data=data, content_type='multipart/form-data', follow_redirects=True, buffered=True, upload_files=[photo])

    # Verifica el redireccionamiento al login
    assert response.status_code == 302
    assert response.location.endswith('/')

def test_agregarTrac_rol_no_reconocido(client):
    # Simula una sesión de usuario con rol no reconocido
    with client.session_transaction() as sess:
        sess['loginCorrecto'] = True
        sess['rol'] = 'UnknownRole'
        sess['documento'] = '123456'

    # Simula una solicitud POST
    data = {
        'idobjeto': '1234',
        'idcategoria': 'Cat1',
        'marca': 'MarcaTest',
        'modelo': 'ModeloTest',
        'fechamodelo': '2024-01-01'
    }
    photo = FileStorage(stream=BytesIO(b'photo_data'), filename='photo.jpg')
    response = client.post('/guardarTractor', data=data, content_type='multipart/form-data', follow_redirects=True, buffered=True, upload_files=[photo])

    # Verifica el redireccionamiento a la página de inicio
    assert response.status_code == 200
    assert b'Rol no reconocido' in response.data

def test_agregarTrac_id_existente(client):
    # Simula una sesión de usuario autenticado como Admin
    with client.session_transaction() as sess:
        sess['loginCorrecto'] = True
        sess['rol'] = 'Admin'
        sess['documento'] = '123456'

    # Simula una solicitud POST con un id ya existente
    data = {
        'idobjeto': 'existing_id',
        'idcategoria': 'Cat1',
        'marca': 'MarcaTest',
        'modelo': 'ModeloTest',
        'fechamodelo': '2024-01-01'
    }
    photo = FileStorage(stream=BytesIO(b'photo_data'), filename='photo.jpg')
    response = client.post('/guardarTractor', data=data, content_type='multipart/form-data', follow_redirects=True, buffered=True, upload_files=[photo])

    # Verifica que se muestra el mensaje de ID ya existente
    assert response.status_code == 200
    assert b'Id ya existente' in response.data
