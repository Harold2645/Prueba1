import datetime
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
<<<<<<< HEAD
from flask import redirect, render_template, request
=======
from email.mime.base import MIMEBase
from email import encoders
from flask import redirect, render_template
>>>>>>> bb083afb6324e7935dfd6f5e195c65d67200a90c
from models.enviosConsu import misEnvios
from routes.graficos import *
from conexion import *
import os


@app.route('/envioConsuPez', methods=['POST'])
def envioConsuPez(): 
    data = misEnvios.datoacpm()
    correoSub = request.form['correoSub']

<<<<<<< HEAD
    guardagrafico()

    remitente = "hangarsena25@outlook.com"
    destinatario = correoSub

    mensaje = """
     <html>
            <body>
                <p>Cordial saludo Estimado,</p>
                <p>Nos dirigimos a usted desde el Centro Agropecuario de Buga SENA CAB, específicamente del equipo encargado del hangar, para informarle que los niveles de combustible diésel disponibles para los tractores están alcanzando sus límites mínimos.</p>
                <p>Es fundamental para nosotros mantener los tractores operativos para asegurar el correcto funcionamiento de nuestras actividades diarias y cumplir con nuestros objetivos. Por ello, solicitamos de manera urgente el reabastecimiento de combustible diésel.</p>
                <p>Adjunto encontrará un gráfico que ilustra los niveles actuales de combustible en nuestra bodega.</p>
                <p>Agradecemos de antemano su pronta atención a esta solicitud y quedamos a la espera de su respuesta.</p>
                <div style="display: flex; align-items: center">
                    <p><img src="cid:logo_sena" alt="Logo SENA" style=" width: 180px;"></p>
                    <div>
                        <p>Atentamente,</p>
                        <p>Equipo de Gestión del Hangar</p>
                        <p>Centro Agropecuario de Buga SENA CAB</p>
                    </div>
                </div>
            </body>
        </html>
    """

    email = MIMEMultipart()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "!!Solicitud Urgente de Reabastecimiento de Combustible Diésel!!"

    # Adjuntar el cuerpo del correo
    email.attach(MIMEText(mensaje, "html"))

    # Ruta de la imagen del logo del SNA
    ruta_logo = os.path.join(app.root_path, 'static', 'img', 'logoSena.png')

    # Adjuntar la imagen como parte del cuerpo del correo
    with open(ruta_logo, 'rb') as archivo_imagen:
        imagen = MIMEImage(archivo_imagen.read())
        # Establecer la Content-ID para que pueda ser referenciada en el cuerpo del correo
        imagen.add_header('Content-ID', '<logo_sena>')
        email.attach(imagen)

    # Adjuntar el gráfico 
    filename = "grafico.pdf"
    with open(filename, "rb") as archivo_grafico:
        adjunto_grafico = MIMEBase("application", "octet-stream")
        adjunto_grafico.set_payload(archivo_grafico.read())
        encoders.encode_base64(adjunto_grafico)
        adjunto_grafico.add_header("Content-Disposition", f"attachment; filename={filename}")
        email.attach(adjunto_grafico)
=======
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
>>>>>>> bb083afb6324e7935dfd6f5e195c65d67200a90c

    # Configurar con servidor 
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "correosena03")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

    return redirect('/graficos')
