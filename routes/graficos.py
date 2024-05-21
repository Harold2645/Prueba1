from flask import redirect, render_template
import matplotlib.pyplot as plt
import io
import numpy as np
import base64
from conexion import *
from models.graficos import misGraficos


@app.route('/graficos')
def graficos():
    return render_template('lideres/graficos/graficos.html')

@app.route('/grafConsu')
def grafConsu():
   
    data = misGraficos.datosConsumibles()

    x = [dato[0] for dato in data]
    y = [dato[1] for dato in data]

    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('Tipos')
    ax.set_ylabel('Cantidad en Bodega')
    plt.savefig("grafico.pdf")
#    return redirect('/graficos')

@app.route('/grafTrac')
def grafTrac():

    data = misGraficos.datosTractores()

    x = [dato[1] for dato in data] #fecha
    y = [dato[0] for dato in data] #cantidad
    nombreT = [dato[2] for dato in data] #nombre

    cantidad_tractores = len(nombreT)

    fig, ax = plt.subplots(figsize=(8, 6))

    # tractores_vistor = set()

    for i in range(cantidad_tractores):
        
        # x_trac = [dato[1] for dato in data if dato[2] == nombreT]
        x_trac = list(range(1, y[i] + 1))
        # y_trac = [dato[0] for dato in data if dato[2] == nombreT]  
        y_trac = [nombreT[i]] * y[i]
        
        ax.plot(x_trac, y_trac, marker="o", label=nombreT[i])
       
    ax.set_xlabel('Fechas')
    ax.set_ylabel('Cantidad de Peticiones')
    ax.set_title('Solicitudes de Tractores')
    ax.legend()

    plt.show()

    return redirect('/graficos')


# data = misGraficos.datosTractores()

#     fig, ax = plt.subplots(figsize=(8, 6))

#     tractores_vistor = set()

#     for dato in data:
#         x = dato[1] #fecha
#         y = dato[0] #cantidad
#         nombreT = dato[2] #nombre
        
#         if nombreT not in tractores_vistor:

#             x_trac = [dato[1] for dato in data if dato[2] == nombreT]
#             y_trac = [dato[0] for dato in data if dato[2] == nombreT]  
            
#             lineas = ax.plot(x_trac, y_trac, label=nombreT)
#             tractores_vistor.add(nombreT)


#     ax.set_xlabel('Fechas')
#     ax.set_ylabel('Cantidad de Peticiones')
#     ax.set_title('Solicitudes de Tractores')
#     ax.legend()

#     plt.show()