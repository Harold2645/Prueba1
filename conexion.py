from datetime import timedelta
import os
from random import randint
from flask import Flask
import mysql.connector

mysql = mysql.connector.connect(user='root', password='', host='localhost', database='hangar')

app = Flask(__name__)
app.secret_key=str(randint(10000,99999))
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes = 3)

CARPETAU = os.path.join('uploads')
app.config['CARPETAU']=CARPETAU
