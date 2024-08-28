import pytest
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Crear la aplicación Flask y la base de datos para pruebas
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Tractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(80), nullable=False)
    modelo = db.Column(db.String(80), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    horas_trabajo = db.Column(db.Integer, nullable=False)
    observaciones = db.Column(db.String(200), nullable=True)

# Rutas para pruebas
@app.route('/agregar_tractor', methods=['GET', 'POST'])
def agregar_tractor():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        horas_trabajo = request.form['horas_trabajo']
        observaciones = request.form['observaciones']

        nuevo_tractor = Tractor(
            marca=marca,
            modelo=modelo,
            anio=anio,
            horas_trabajo=horas_trabajo,
            observaciones=observaciones
        )
        db.session.add(nuevo_tractor)
        db.session.commit()
        return redirect(url_for('listar_tractores'))
    
    return render_template('tractoresAg.html')

@app.route('/listar_tractores', methods=['GET'])
def listar_tractores():
    tractores = Tractor.query.all()
    return render_template('listar_tractores.html', tractores=tractores)

# Pruebas con pytest
@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.drop_all()

def test_agregar_tractor(client):
    response = client.post('/agregar_tractor', data={
        'marca': 'John Deere',
        'modelo': 'X540',
        'anio': '2024',
        'horas_trabajo': '120',
        'observaciones': 'En buen estado'
    })
    assert response.status_code == 302  # Redirección
    assert Tractor.query.count() == 1
    tractor = Tractor.query.first()
    assert tractor.marca == 'John Deere'
    assert tractor.modelo == 'X540'
    assert tractor.anio == 2024
    assert tractor.horas_trabajo == 120
    assert tractor.observaciones == 'En buen estado'

def test_formulario_agregar_tractor(client):
    response = client.get('/agregar_tractor')
    assert response.status_code == 200
    assert b'Agregar Tractor' in response.data
