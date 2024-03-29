from models.enviosConsu import misEnvios
from email.message import EmailMessage
import smtplib

def envioConsuPez():

    data = misEnvios.envioConsuPez()
 
    

    remitente = "hangarsena23@outlook.com"
    destinatario = "padilla2645@gmail.com"
    mensaje = "urbano no se baña "
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



