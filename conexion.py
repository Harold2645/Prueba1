from datetime import timedelta
import os
from random import randint
from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(user='root', password='', host='localhost', database='freedb_hangar0.2')

app = Flask(__name__)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 15)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
