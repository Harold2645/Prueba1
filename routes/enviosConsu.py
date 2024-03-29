import datetime
import smtplib
from email.message import EmailMessage
from flask import redirect, render_template
from models.enviosConsu import misEnvios
from conexion import *

@app.route('/graficos')
def graficos():
    return render_template('lideres/graficos/graficos.html')


@app.route('/envioConsuPez')
def envioConsuPez(): 

    data = misEnvios.datoacpm()
    if data and data[0][0] <= 25:
        remitente = "hangarsena23@outlook.com"
        destinatario = "padilla2645@gmail.com"
        mensaje = "El ACPM esta en los minimos recomendados Mande mas "
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["subject"] = "correo de prueba"
        email.set_content(mensaje)
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(remitente,"chicastrans69")
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()

    return redirect('/graficos')

 

# echo "/desarrollo-hg/hangar-sis/proyecHangar/Prueba1/routes/enviosConsu.py" | at 11:30am

# schtasks /create /tn "EjecutarEnviosConsu" /tr "C:\Python\python.exe C:\desarrollo-hg\hangar-sis\proyecHangar\Prueba1\routes\enviosConsu.py" /sc once /st 11:30 /ru SYSTEM

# schtasks /delete /tn "EjecutarEnviosConsu" /f
