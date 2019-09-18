import requests

from flask import render_template
from app import app
from app.functions.read_only import *
from app.functions.rw import *

@app.route('/', methods=['GET'])
def index():
    """
    This is a route that grabs all the database data and prints to console. 
    """
    get_all_data_postgres()
    return render_template('mainpage.html', title='Main')

@app.route('/import_database', methods=['GET'])
def import_data():
    """
    Route to import data from csv to data base. Only should be ran once to build database.
    """
    try:
        import_database()
    except:
        print("There was an issue importing the database.")

@app.route('/top_ten_movies', methods=['GET'])
def top_ten():
    """
    This route returns the top ten movies based on highest grossing film
    """
    get_top_ten_grossest()
    return render_template('mainpage.html', title='Main')

@app.route('/top_ten_directors', methods=['GET'])
def top_ten_directors():
    """
    This route prints top ten directors based on highest grossing film and no duplicates 
    """
    get_top_ten_directors()
    return render_template('mainpage.html', title='Main')
    