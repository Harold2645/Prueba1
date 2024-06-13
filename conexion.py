from datetime import timedelta
import os
from random import randint
from flask import Flask
import mysql.connector

<<<<<<< HEAD
conexion = mysql.connector.connect(user='root', password='', host='localhost', database='hangarbd')
=======
conexion = mysql.connector.connect(user='root', password='', host='localhost', database='hangar')
>>>>>>> bb083afb6324e7935dfd6f5e195c65d67200a90c

app = Flask(__name__)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 15)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
