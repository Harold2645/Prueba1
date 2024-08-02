from datetime import timedelta
import os
from random import randint
from flask import Flask
from flask_cors import CORS
import mysql.connector

#conexion = mysql.connector.connect(user='hangar', password='H4ng4r', host='85.31.231.136', database='hangarbd')
conexion = mysql.connector.connect(user='root', password='', host='localhost', database='hangarbd') 

app = Flask(__name__)
CORS(app)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 15)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
