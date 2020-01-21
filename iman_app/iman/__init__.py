import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2820d3108d6656cdd809a4d88e92d8d'
UPLOAD_FOLDER = 'iman/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from iman import routes