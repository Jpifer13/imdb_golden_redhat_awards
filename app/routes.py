import requests

from flask import render_template
from app import app
from app.functions.read_only import *
from app.functions.rw import *

@app.route('/', methods=['GET'])
def index():
    get_all_data_postgres()
    # data = get_data()
    # for key in data.iloc[2].items():
    #     print(key[0])
    # print(data.iloc[2])
    # print(data.text)
    return render_template('mainpage.html', title='Main')

@app.route('/import_database', methods=['GET'])
def import_data():
    try:
        import_database()
    except:
        print("There was an issue importing the database.")

@app.route('/top_ten_movies', methods=['GET'])
def top_ten():
    get_top_ten_grossest()
    return render_template('mainpage.html', title='Main')

@app.route('/top_ten_directors', methods=['GET'])
def top_ten_directors():
    get_top_ten_directors()
    return render_template('mainpage.html', title='Main')
    