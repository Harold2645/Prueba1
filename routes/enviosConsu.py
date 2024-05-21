import datetime
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from flask import redirect, render_template
from models.enviosConsu import misEnvios
from routes.graficos import *
from conexion import *

@app.route('/envioConsuPez')
def envioConsuPez(): 

    data = misEnvios.datoacpm()

    grafConsu()
#    grafico.show()

    #grafico = io.BytesIO()
    # grafico.savefig("grafico.pdf")
#    grafico.seek(0)

    #imgrafico = base64.b64encode(grafico.read()).decode('utf-8')

    # if data and data[0][0] <= 25:
    remitente = "hangarsena24@outlook.com"
    destinatario = "padilla2645@gmail.com"
    mensaje = "Aqui se muestra la cantidad de conbusible que hay bodega solicitamos mas"

    email = MIMEMultipart()
    email["From"] = remitente
    email["To"] = destinatario
    email["subject"] = "correo de prueba"

    body = MIMEText(mensaje)
    email.attach(body)
    filename = "grafico.pdf"
    attachment = open(filename, "rb")
    # The instance of MIMEBase and named as p
    p = MIMEBase("application", "octet-stream")
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    email.attach(p)


    #img = MIMEImage(base64.b64decode(imgrafico), name='grafico.png')
    #email.attach(p)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente,"correosena03")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
    return redirect('/graficos')
    # else:
    #     return redirect('/funciones')

 

# echo "/desarrollo-hg/hangar-sis/proyecHangar/Prueba1/routes/enviosConsu.py" | at 11:30am

# schtasks /create /tn "EjecutarEnviosConsu" /tr "C:\Python\python.exe C:\desarrollo-hg\hangar-sis\proyecHangar\Prueba1\routes\enviosConsu.py" /sc once /st 11:30 /ru SYSTEM

# schtasks /delete /tn "EjecutarEnviosConsu" /f
