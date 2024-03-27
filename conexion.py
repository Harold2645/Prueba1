from datetime import timedelta
import os
from random import randint
from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(user='freedb_hangar0.2', password='3Rde#r5E5EJU%YK', host='sql.freedb.tech', database='freedb_hangar0.2')

app = Flask(__name__)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 3)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
