from flask import redirect, render_template
import matplotlib.pyplot as plt
import io
from conexion import *


@app.route('/graficos')
def graficos():
    return render_template('lideres/graficos/graficos.html')

@app.route('/grafConsu')
def grafConsu():
    cursor = mysql.cursor()
    sql = "SELECT nombre, cantidad FROM consumibles "\
          "GROUP BY nombre ORDER BY nombre ASC"
    cursor.execute(sql)
    data = cursor.fetchall()
    mysql.close()

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

    # cursor = mysql.cursor()
    # sql = "SELECT nombre, cantidad, fechasalida FROM servicios  "\
    #       "INNER JOIN "


    return redirect('/graficos')