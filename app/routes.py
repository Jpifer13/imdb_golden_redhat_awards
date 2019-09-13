import requests

from flask import render_template
from app import app
from app.functions.read_only import *

@app.route('/', methods=['GET'])
def index():
    data = get_data()
    print(data.head())
    # print(data.text)
    return render_template('mainpage.html', title='Main')