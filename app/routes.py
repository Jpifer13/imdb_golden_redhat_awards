import requests

from flask import render_template
from app import app
from app.functions.read_only import *

@app.route('/', methods=['GET'])
def index():
    data = get_data()
    for key in data.iloc[2].items():
        print(key[0])
    print(data.iloc[2])
    # print(data.text)
    return render_template('mainpage.html', title='Main')