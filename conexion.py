from datetime import timedelta
import os
from random import randint
from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(user='hangar', password='H4ng4r', host='localhost', database='hangarbd')

app = Flask(__name__)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 15)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
