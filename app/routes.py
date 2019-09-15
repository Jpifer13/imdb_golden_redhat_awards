import requests

from flask import render_template
from app import app
from app.functions.r import *
from app.functions.rw import *

@app.route('/', methods=['GET'])
def index():
    # data = import_database()
    
    # print(data.text)
    return render_template('mainpage.html', title='Main')