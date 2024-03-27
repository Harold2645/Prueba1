from flask import redirect, render_template
import matplotlib.pyplot as plt
import io
import numpy as np
from conexion import *


@app.route('/graficos')
def graficos():
    return render_template('lideres/graficos/graficos.html')

@app.route('/grafConsu')
def grafConsu():
    cursor = conexion.cursor()
    sql = "SELECT nombre, cantidad FROM consumibles "\
          "GROUP BY nombre ORDER BY nombre ASC"
    cursor.execute(sql)
    data = cursor.fetchall()
    conexion.close()

    x = [dato[0] for dato in data]
    y = [dato[1] for dato in data]

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('Tractores')
    ax.set_ylabel('Cantidad en Bodega')

    plt.show()

    return redirect('/graficos')

@app.route('/grafTrac')
def grafTrac():

    cursor = conexion.cursor()
    sql = "SELECT tractores.marca, servicios.cantidad, servicios.fechasalida, COUNT(*) FROM servicios  "\
          "INNER JOIN tractores ON servicios.idobjeto = tractores.idobjeto "\
          "GROUP BY tractores.marca ORDER BY tractores.marca ASC"
    cursor.execute(sql)
    data = cursor.fetchall()
    conexion.close()

    # fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
    # np.random.seed(19680801)

    x = [dato[0] for dato in data]
    y = [dato[1] for dato in data]
    z = [dato[2] for dato in data]

    fig, ax = plt.subplots(figsize=(8, 6))

    # linesy = ax.plot(x, z, label='Tractor Ferguson')

    ax.scatter(z, y, label='[FALTA ESTO]')

    ax.set_xlabel('Fechas De Salida')
    ax.set_ylabel('Cantidad De Peticiones')
    ax.set_title('GRAFICO DE PETIONES MENSUAL')
    ax.legend()

    plt.show()

    fig, ax =plt.subplot(figsize=(5, 3), layout='constrained')
    np.random.seed(19680801)



    return redirect('/graficos')