from flask import redirect, render_template, session
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import numpy as np
import base64
from conexion import *
from models.graficos import misGraficos
import matplotlib.dates as mdates


@app.route('/graficos')
def graficos():

    if session.get("loginCorrecto"):
        rol = session['rol'] 
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            return render_template('lideres/graficos/graficos.html',nombreusu=nombre  , rolusu=rol )
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


@app.route('/guardagrafico')
def guardagrafico():

    if session.get("loginCorrecto"):
        rol = session['rol'] 
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
               
            data = misGraficos.datosConsumibles()

            species = [dato[0] for dato in data]
            existing = [dato[1] for dato in data]

            max_qty = [100] * len(species)  # Cantidad máxima por defecto
            min_qty = [20] * len(species)   # Cantidad mínima por defecto

            penguin_means = {
                'Cantidad Max': max_qty,
                'Existente': existing,
                'Cantidad Min': min_qty,
            }

            x = np.arange(len(species))
            width = 0.25
            multiplier = 0

            fig, ax = plt.subplots(layout='constrained')

            for attribute, measurement in penguin_means.items():
                offset = width * multiplier

                if attribute == 'Cantidad Max':
                    color = 'gray'
                elif attribute == 'Cantidad Min':
                    color = 'orange'
                elif attribute == 'Existente':
                    colors_list = []
                    for i, value in enumerate(measurement):
                        if value > penguin_means['Cantidad Min'][i]:
                            colors_list.append('green')
                        else:
                            colors_list.append('red')

                    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors_list)
                    ax.bar_label(rects, padding=3)
                    multiplier += 1
                    continue

                rects = ax.bar(x + offset, measurement, width, label=attribute, color=color)
                ax.bar_label(rects, padding=3)
                multiplier += 1

            ax.set_ylabel('Unidad de Medida "Galones"')
            ax.set_title('Niveles de Líquidos del Hangar')
            ax.set_xticks(x + width, species)
            ax.legend(loc='upper right', ncols=1)
            ax.set_ylim(0, 110)
            plt.savefig("grafico.pdf")

        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')


@app.route('/grafConsu')
def grafConsu():  
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        nombre = session['nombreUsuario']
        if rol in ['Admin', 'Practicante']:
            data = misGraficos.datosConsumibles()

            species = [dato[0] for dato in data]
            existing = [dato[1] for dato in data]

            
            max_qty = [100] * len(species)  # Cantidad máxima por defecto
            min_qty = [20] * len(species)   # Cantidad mínima por defecto

            penguin_means = {
                'Cantidad Max': max_qty,
                'Existente': existing,
                'Cantidad Min': min_qty,
            }

            x = np.arange(len(species))
            width = 0.25
            multiplier = 0

            fig, ax = plt.subplots(layout='constrained')

            for attribute, measurement in penguin_means.items():
                offset = width * multiplier

                if attribute == 'Cantidad Max':
                    color = 'gray'
                elif attribute == 'Cantidad Min':
                    color = 'orange'
                elif attribute == 'Existente':
                    colors_list = []
                    for i, value in enumerate(measurement):
                        if value > penguin_means['Cantidad Min'][i]:
                            colors_list.append('green')
                        else:
                            colors_list.append('red')

                    rects = ax.bar(x + offset, measurement, width, label=attribute, color=colors_list)
                    ax.bar_label(rects, padding=3)
                    multiplier += 1
                    continue

                rects = ax.bar(x + offset, measurement, width, label=attribute, color=color)
                ax.bar_label(rects, padding=3)
                multiplier += 1

            ax.set_ylabel('Unidad de Medida "Galones"')
            ax.set_title('Niveles de Líquidos del Hangar')
            ax.set_xticks(x + width, species)
            ax.legend(loc='upper right', ncols=1)
            ax.set_ylim(0, 110)

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            img_buf.seek(0)
            img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
            plt.close(fig)

            return render_template('lideres/graficos/graficos.html', img_base64=img_base64, nombreusu=nombre, rolusu=rol)
        else:
            return redirect('/panel')
    else:
        return redirect('/')


@app.route('/grafTrac')
def grafTrac():
    if session.get("loginCorrecto"):
        rol = session['rol'] 
        nombre = session['nombreUsuario']
        if rol == 'Aprendiz' or rol == 'Instructor' or rol == 'Trabajador':
            return redirect('/panel')
        elif rol == 'Admin' or rol == 'Practicante':
            data = misGraficos.datosTractores()

            fig, ax = plt.subplots(figsize=(8, 6))

            tractores_vistor = set()
            all_dates = set()  # Para almacenar todas las fechas
            tractor_data = {}  # Para acumular datos por tractor

            for dato in data:
                x = dato[1]  # fecha
                y = dato[0]  # cantidad
                nombreT = dato[2]  # nombre

                # Acumular fechas
                all_dates.add(x)

                # Agrupar datos por tractor
                if nombreT not in tractor_data:
                    tractor_data[nombreT] = {}
                if x not in tractor_data[nombreT]:
                    tractor_data[nombreT][x] = 0
                tractor_data[nombreT][x] += y

            # Generar las líneas del gráfico
            for nombreT, fechas in tractor_data.items():
                x_trac = []
                y_trac = []
                for fecha in sorted(all_dates):
                    x_trac.append(fecha)
                    y_trac.append(fechas.get(fecha, 0))  # Mantener en 0 si no hay solicitudes

                lineas = ax.plot(x_trac, y_trac, label=nombreT)
                tractores_vistor.add(nombreT)

            # Formatear el eje X para mostrar solo la fecha
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Mostrar una fecha cada dos días
            ax.tick_params(axis='x', labelsize=8)  # Ajustar tamaño de las etiquetas del eje X

            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')  # Rotar etiquetas

            ax.set_xlabel('Fechas')
            ax.set_ylabel('Cantidad de Peticiones')
            ax.set_title('Solicitudes de Tractores')
            ax.legend()

            # Save the plot to a BytesIO object
            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            img_buf.seek(0)
            img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

            plt.close(fig)

            return render_template('lideres/graficos/graficos.html', img_base64=img_base64, nombreusu=nombre, rolusu=rol)
        else:
            return render_template("index.html", msg="Rol no reconocido")
    else:
        return redirect('/')