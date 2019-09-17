import requests

from flask import render_template
from app import app
from app.functions.r import *
from app.functions.rw import *

@app.route('/', methods=['GET'])
def index():
    # data = import_database()
    
    data = get_data()
    for key in data.iloc[2].items():
        print(key[0])
    print(data.iloc[2])
    return render_template('mainpage.html', title='Main')