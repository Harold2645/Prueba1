from conexion import *
from datetime import datetime

import pytest

from models.categorias import misCategorias

class Test_categorias:

    ahora = datetime.now()


    @pytest.mark.parametrize(
        ["nombre","tipo","descripcion", "fecha","creador","esperado"],
        [("Tractor","Tractor","Aqui hay tractores",ahora,"1234567890",True),
        ("Martillo Pesado","Herramienta","Aqui hay martillos pesados",ahora,"1234567890",True),
        ("Clavos","Insumo","Aqui hay clavos de 3cm",ahora,"1234567890",True),
        ("Aceite","Liquido","Aqui hay aceites de todo tipo",ahora,"1234567890",True),]
    )
    def test_agregar_categoria(self,nombre,tipo,descripcion, fecha,creador, esperado):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.agregarCategoria(nombre,tipo,descripcion, fecha,creador)
        # Verificar resultados
        assert resultado == esperado

    def test_todas_categorias(self):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.consultarCategorias()
        # Verificar resultados
        assert len(resultado) == 4

    def test_categorias_tractor(self):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.categoriasTractor()
        # Verificar resultados
        assert len(resultado) == 1
        return Test_categorias.test_eliminar_categoria(resultado)

    def test_categorias_herramienta(self):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.categoriasHerramienta()
        # Verificar resultados
        assert len(resultado) == 1

        

    def test_categorias_insumo(self):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.categoriasInsumos()
        # Verificar resultados
        assert len(resultado) == 1

    def test_categorias_liquido(self):
        # Ejecutar el método a probar (la prueba)
        resultado = misCategorias.categoriasLiquidos()
        # Verificar resultados
        assert len(resultado) == 1

    def test_eliminar_categoria(self,resultado):
        res = resultado[0]
        eliminar = misCategorias.borrarCategoria(res)
        assert eliminar == True